
import  descargar_csv
import pandas as pd
from unificar_datos import obtener_parametros, generar_tablas, depurar_tablas
from interfaz_bbdd import conexion_bbdd,ejecutar,insertar,carga_cines,calculo_total
from registros import registrar


if __name__ == "__main__":

# Conexion a la base de datos, los siguientes parametros se corresponden a la configuración de la misma
# u_challenge1 : usuario de la bbdd
# password_challenge1: contraseña para la bbdd
# localhost : ubicación de la bbdd
# 5432 : puerto habilitado por el servidor de bbdd
# challenge1: nombre de la bbdd

#Inicializo el motor de logging
registrar()


    conexion=conexion_bbdd("u_challenge1", "password_challenge1", "localhost", 5432, "challenge1")
logging.info("Conexion con la bbdd correcta ")
# Se declara una lista de parametros para el analisis de los archivos
    parametros=obtener_parametros()
# Se genera una lista de tablas con los registros de las fuentes    
    tabla1=generar_tablas(parametros)
# Defino las columnas que se trabajaran en la tabla de datos Agrupados    
    columnas= ['Cod_Loc','IdProvincia','IdDepartamento','categoria','provincia','localidad','nombre','direccion','CP','telefono','mail','web']
# Filtro las tablas de la lista de tablas con las columnas indicadas
    t1,t2,t3=depurar_tablas(tabla1,columnas)
# Genero una nueva tabla con todos los registros unificados
    agrupados= pd.concat([t1,t2,t3])

# Se eliminan los registros de las tablas antes de guardar registros nuevos
    try:
     ejecutar(conexion,"delete from public.\"T_Agrupados\"")
     print("Registros de Agrupados eliminados correctamente")
     ejecutar(conexion,"delete from public.\"T_Cines\"")
     print("Registros de Cines eliminados correctamente")
     ejecutar(conexion,"delete from public.\"T_Total\"")
     print("Registros de Totales eliminados correctamente")
    except:
     pass
    finally:
    
    # Inserto los registros de la tabla unificada generada en la base de dato
     insertar(conexion,"T_Agrupados",agrupados)
    # Calculo e inserto los registros propios de Cine
     carga_cines(conexion)
    # Calculo e inserto los registros propios de calculo total
     calculo_total(conexion)





