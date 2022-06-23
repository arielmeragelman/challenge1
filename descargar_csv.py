

def download_file(url,categoria):
# Funcion de descarga de archivos csv (fuente de datos) -
#  Input> url: url completa donde esta el archivo  - categoria: categoria que le asignaremos a dicha información
#  Output: N/A
# Descarga el archivo csv de la url especificada en un directorio/nombre con el formato  ./categoria/mes_año/categoria-dia-mes-año.csv 
# Version: 1.0 - Sebastian Meragelman

  import requests
  from datetime import datetime

  date = datetime.now()
  year_month = date.strftime('%Y-%m')
  day_month_year  = date.strftime('%d-%m-%Y')


  ubicacion=categoria+"\\"+year_month+"\\"
  nombre=categoria+"-"+day_month_year+".csv"
    
  crear_directorios(ubicacion)  

  response = requests.get(url)  
  open(ubicacion+nombre, "wb").write(response.content)


def crear_directorios(nuevo_dir):
# Funcion de creacion de arbol de directorios -
#  Input> nuevo_dir : path del directorio a crear, es posible usar path completos o relativos
#  Output: N/A
# En caso de no existir el arbol de directorios lo crea, de existir omite el paso  
# Version: 1.0 - Sebastian Meragelman

    import os
    os.makedirs(nuevo_dir, exist_ok = True)
    
def download_files():
# Funcion de descarga de archivos csv con parametros pre establecidos  (fuente de datos) -
#  Input> N/A
#  Output: N/A
# Tiene parametrizados 3 fuentes de datos y 3 categorias, ejecutara las llamadas a funciones  
# Version: 1.0 - Sebastian Meragelman    
   

   #INICIO PARAMETROS QUE PODRIAN MODIFICARSE: 
    museos="https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
    cine="https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
    biblioteca="https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"

    archivos= [(museos,"museos"),(cine,"cine"),(biblioteca,"biblioteca")]
   #FIN PARAMETROS QUE PODRIAN MODIFICARSE:


    for url,categoria in archivos:
        download_file(url,categoria)
        
        
        
# INICIO SECUENCIA DE EJECUCION        
download_files()


