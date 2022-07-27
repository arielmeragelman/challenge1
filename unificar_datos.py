from typing import MutableSequence
import pandas as pd
from registros import registrar
logging=registrar()



def abrir_csv(categoria,anio,mes,dia):
# Funcion lectura de archivos csv (fuente de datos) -
#  Input> categoria: categoria de la fuente a abrir  - anio,mes,dia : fecha de la fuente a consultar (Y,mm,dd) 
#  Output: Un objeto pandas con todos los registros formateados como csv, cada salto de linea sera una fila y cada comma una columna 
# Abre con la libreria de pandas el archivo ./categoria/mes_año/categoria-dia-mes-año.csv y lo convierte en un objeto pandas (arreglo matricial/serie) 
# Version: 1.0 - Sebastian Meragelman

    ubicacion=categoria+"\\"+anio+"-"+mes+"\\"
    nombre=categoria+"-"+dia+"-"+mes+"-"+anio+".csv"
    archivo = ubicacion + nombre 
    return pd.read_csv(archivo)





def obtener_parametros():
# Funcion da formato a los parametros que necesitemos para trabajar los datos -
#  Input> N/A 
#  Output: Tupla con 2 tuplas, la primera contiene las categorias que parametrizamos, a segunda tupla contendra dia,mes,año 
# ! La funcion devuelve las categorias harcodeadas, para la version v1.1 se debe de crear una lista categoria con un ciclo ue tome todos los valores que el usuario necesite y retornar como lista  
# Version: 1.0 - Sebastian Meragelman


    from datetime import datetime
    date = datetime.now()
    
    dia=date.strftime('%d')
    mes=date.strftime('%m')
    anio= date.strftime('%Y')
    categorias=("biblioteca","cine","museos")
    
    return ((categorias[0],categorias[1],categorias[2]),(anio,mes,dia))


def generar_tablas(parametros):
# Funcion generar una tupla con objetos pandas y su categoria -
#  Input> parametros: es la lista de categorias que se analizaran y la fecha de dicha fuente
#  Output> tablas: devuelve una lista de objetos pandas que contienen los datos leidos de los csv   
# La funcion recorre una lista de categorias para una fecha determinada y arma una lista con los objetos resultantes  
# Version: 1.0 - Sebastian Meragelman

    if not (parametros[0][0] and parametros[1][0] and parametros[1][1] and parametros[1][2] ):
        logging.error("No estan definidos todos los parametros necesarios")
    logging.info("parametros: "+str(parametros))

    tablas=[]
    for cat in parametros[0]:
        try:
            tablas.append(abrir_csv(cat,parametros[1][0],parametros[1][1],parametros[1][2]))        
        except:
                logging.error("No se pudo abrir el archivo csv")
    return tablas

def agregar_timestamp(tabla):
# Funcion crea una columna a partir del objeto pandas con el timestamp de cuando se ejecuta la consulta 
#  Input> tabla: objeto pandas para trabajar 
#  Output: objeto pandas de tamaño 1xN  donde N sera la cantidad de registros del objeto pandas 
# La funcion obtiene el timestamp del momento de ejecucion y lo asigna a un objeto pandas con la forma 1xN  
# Version: 1.0 - Sebastian Meragelman
   
    from datetime import datetime
    dt=datetime.now()
    ts=datetime.timestamp(dt)
    try:
        tabla['modifica'] =  ts
    except:
        logging.error("El objeto tabla no es un dataframe")
    return tabla['modifica']


def timestamp(tabla):
# Funcion crea una columna a partir del objeto pandas con el timestamp de cuando se ejecuta la consulta 
#  Input> tabla: objeto pandas para trabajar 
#  Output: objeto pandas de tamaño 1xN  donde N sera la cantidad de registros del objeto pandas 
# La funcion obtiene el timestamp del momento de ejecucion y lo asigna a un objeto pandas con la forma 1xN  
# Version: 1.0 - Sebastian Meragelman
   
    from datetime import datetime
    dt=datetime.now()
    ts=datetime.timestamp(dt)
    try:
        tabla = tabla.assign(Timestamp=ts)
        return tabla
    except:
        logging.error("El objeto tabla no es un dataframe")
        exit()





    


def depurar_tablas(tabla,columnas):
# Funcion redefine la estructura de una tabla segun la lista de columnas que se le indiquen 
#  Input> tabla: objeto pandas para trabajar - columnas: lista de columnas que vamos a filtrar 
#  Output: una lista de objetos pandas de tamaño (M+1)xN  donde la ultima columna agregada es la fecha de modificacion 
# La funcion filtra el dataframe y devuelve un nuevo objeto con las columnas seleccionadas  
# Version: 1.0 - Sebastian Meragelman

    if type(columnas) != list:  
        logging.error("El objeto columnas no es una lista con las columnas")
        exit()

    #Se utiliza un diccionario para corresponder cada identificador de columna con una ubicación de columna para cada tabla
    museos_dic = dict()
    biblioteca_dic = dict()
    cines_dic = dict()

    # Lista de indices para usar en los DataFrame
    museos_ix= []
    biblioteca_ix= []
    cines_ix= []
    
    try:
        #Defino los diccionarios
        museos_dic = {'Cod_Loc' : 0,'IdProvincia' : 1,'IdDepartamento' : 2,'Observaciones' : 3,'categoria' : 4,'subcategoria' : 5,'provincia' : 6,'localidad' : 7,'nombre' : 8,'direccion' : 9,'piso' : 10,'CP' : 11,'cod_area' : 12,'telefono' : 13,'mail' : 14,'web' : 15,'Latitud' : 16,'Longitud' : 17,'TipoLatitudLongitud' : 18,'Info_adicional' : 19,'fuente' : 20,'jurisdiccion' : 21,'a_inauguracion' : 22,'actualizacion' : 23
        }
        #Cargo los indices usando el diccionario
        for i in columnas:
            try:
            
                museos_ix.append(museos_dic[i])
            except:
                pass

    

        
        
        biblioteca_dic = {'Cod_Loc' : 0,'IdProvincia' : 1,'IdDepartamento' : 2,'Observaciones' : 3,'categoria' : 4,'subcategoria':5,'provincia' : 6,'Departamento' : 7,'localidad' : 8,'nombre' : 9,'direccion' : 10,'piso' : 11,'CP' : 12,'cod_area' : 13,'telefono' : 14,'mail' : 15,'web' : 16,'Info_adicional' : 17,'Latitud' : 18,'Longitud' : 19,'TipoLatitudLongitud' : 20,'fuente' : 21,'Tipo_gestion' : 22,'a_inauguracion' : 23,'actualizacion' : 24
        }

        for i in columnas:
            try:
                biblioteca_ix.append(biblioteca_dic[i])
            except:
                pass

            cines_dic = {'Cod_Loc':0, 'IdProvincia':1, 'IdDepartamento':2, 'Observaciones':3,'categoria':4, 'provincia':5, 'Departamento':6, 'localidad':7, 'nombre':8,'direccion':9, 'piso':10, 'CP':11, 'cod_area':12, 'telefono':13, 'mail':14, 'web':15,'Info_adicional':16, 'Latitud':17, 'Longitud':18, 'TipoLatitudLongitud':19,'fuente':20, 'tipo_gestion':21, 'Pantallas':22, 'Butacas':23, 'espacio_INCAA':24,'actualizacion':25}

        for i in columnas:
            cines_ix.append(cines_dic[i])
        
    except:
        logging.error("Hay columnas que no figuran en la definicion del diccionario")

        
    #Realizo el filtrado de columnas y la conversión de registros vacios por "NULL"
    tabla[2] = tabla[2].iloc[:,museos_ix].fillna("NULL")
    tabla[0] = tabla[0].iloc[:,biblioteca_ix].fillna("NULL")
    tabla[1] = tabla[1].iloc[:,cines_ix].fillna("NULL")

    #Realizo una limpieza de registros no nulos pero con información sin utilidad
    tabla[0]=tabla[0].replace("s/d","NULL")
    tabla[1]=tabla[1].replace("s/d","NULL")
    tabla[2]=tabla[2].replace("s/d","NULL")
    
    #Defino el nuevo nombre de las columnas
    #Se aplica una clausula try para poder reusar el codigo en una sola de las tablas o en todas
    try:
        tabla[0].columns = columnas
        tabla[1].columns = columnas
        tabla[2].columns = columnas
        
        
    except:
        pass
    
    
    
    
    #Agrego una columna con el tiempo de modificacion
    for i,v in enumerate(tabla):
        
        #tabla[i] = agregar_timestamp(v)        
        tabla[i] = timestamp(tabla[i])
        
    return tabla
