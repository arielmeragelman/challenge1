import pandas as pd
from unificar_datos import generar_tablas
from unificar_datos import obtener_parametros,depurar_tablas
from registros import registrar

registrar()


def conexion_bbdd(user, passwd, host, port, db):
# Funcion encargada de establecer la conexion con la bbdd 
#  Input> user: usuario bbdd - passwd: contraseña bbdd - host : ubicacion de la bbdd - port : puerto habilitado - db: nombre de la bbdd 
#  Output: Un objeto sqlalchemy con la conexion a la bbdd 
# La funcion establece la conexion de la bbdd  
# Version: 1.0 - Sebastian Meragelman

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    try:
        engine = create_engine(url, pool_size=50, echo=False)
    except:
        logging.error("No se establecio la conexion con la bbdd url: "+url)
    
    return engine



def ejecutar(engine,consulta):
# Funcion ejecuta la consulta sql en la bbdd 
#  Input> engine: objeto sqlalchemy con la conexion - consulta: consulta sl 
#  Output: Devuelve un objeto sqlalchemy con el resultado de la ejecucion, no de la consulta 
# Funcion ejecuta la consulta sql en la bbdd  
# Version: 1.0 - Sebastian Meragelman

    return engine.execute(consulta)

def insertar(engine,n_tabla,tabla):
# Funcion ejecuta un insert de un objeto dataframe en una tabla sql 
#  Input> engine: objeto sqlalchemy con la conexion - n_tabla : nombre de la tabla de la bbdd - tabla: objeto dataframe
#  Output: N/a 
# Funcion inserta en la bbdd el objeto dataframe creando una tabla de no existir o agregando nuevos registros si los existieran  
# Version: 1.0 - Sebastian Meragelman

    tabla.to_sql(n_tabla, engine, if_exists='append' ,schema='public')

    

def limpiar_tabla(engine,t_bbdd):
# Funcion ejecuta una funcion almacenada en la bbdd para eliminar registros de la tabla
#  Input> engine: objeto sqlalchemy con la conexion - t_bbdd: nombre de la tabla 
#  Output: N/a 
# Funcion ejecuta la consulta sql en la bbdd  
# Version: 0.1 - Sin probar - Sebastian Meragelman

    consulta="select limpiar_tabla(\'public.\""+t_bbdd+ "\"\');"
    print(consulta)
    print(ejecutar(engine,consulta))


def carga_cines(conexion):
# Funcion formatea registros de las fuentes y las carga en la bbdd 
#  Input> conexion: objeto sqlalchemy con la conexion
#  Output: N/a 
# Funcion Establece una serie de columnas particulares para analizar, sobre esto realiza un calculo y las carga en la bbdd en una tabla propia   
# Version: 1.0 - Sebastian Meragelman


    columnas= ['provincia','Pantallas','Butacas','espacio_INCAA']
    parametros=obtener_parametros()
    tabla1=generar_tablas(parametros)

    t1,t2,t3=depurar_tablas(tabla1,columnas)
    t2['espacio_INCAA']=t2['espacio_INCAA'].replace({'NULL':0,'0':0,'si':1,'SI':1})
    t2=t2.groupby("provincia").agg({columnas[1]:['sum'],columnas[2]:['sum'],columnas[3]:['sum']}).reset_index(level=0)
    insertar(conexion,"T_Cines",t2)
    

    
def calculo_total(conexion):
# Funcion inserta en la bbdd una tabla con resultados de calculos a partir de las fuentes csv 
#  Input> conexion: objeto sqlalchemy con la conexion
#  Output: N/a 
# Funcion Establece una serie de columnas particulares para analizar, sobre esto realiza un calculo y las carga en la bbdd en una tabla propia  
# Version: 1.0 - Sebastian Meragelman
    
    columnas= ['provincia','fuente','categoria']
    parametros=obtener_parametros()
    tabla1=generar_tablas(parametros)

    t1,t2,t3=depurar_tablas(tabla1,columnas)
    
    #Unimos las 3 fuentes en un mismo dataframe
    t= pd.concat([t1,t2,t3])

    #Obtenemos 3 dataframes a partir de la agrupacion y conteo de registros
    ta=t.groupby(['categoria'])['categoria'].count()
    tb=t.groupby(['provincia'])['provincia'].count()
    tc=t.groupby(['fuente'])['fuente'].count()
    #Genero una copia del dataframe para no alterarlo
    td=t
    #Genero una nueva columna con el concatenado de prov y categ para generar una clase nueva en conjunto
    td['concat']=t['provincia']+t['categoria']
    #A partir de esta nueva clase genero un recuento
    td=td.groupby(['concat'])['concat'].count()
    #Defino un nuevo dataframe de dimenciones 2xN donde N es la cantidad de registros total entre todos los dataframe concatenados
    t= pd.concat([ta,tb,tc,td])


    insertar(conexion,"T_Total",t)