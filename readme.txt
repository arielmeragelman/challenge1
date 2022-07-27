ir al directorio donde se vaya a crear el entorno virtual para la app

virtualenv challenge1

cd directorio_virtual/challenge1/Scripts/
./activate

pip install SQLAlchemy and pip install psycopg2
pip install requests
pip install pandas
pip install python-decouple

Error de conexion ssl para la descarga de archivos csv con request

---- estos pasos se siguieron se resolvio el problema, copiar archivos dll de bin a dll-----
https://github.com/conda/conda/issues/8273
---------------------------------------------------------------
El entorno virtual con el cual se ejecuto el deploy reporta

pip freeze
certifi==2022.6.15
charset-normalizer==2.0.12
greenlet==1.1.2
idna==3.3
numpy==1.22.4
pandas==1.4.2
psycopg2==2.9.3
python-dateutil==2.8.2
python-decouple==3.6
pytz==2022.1
requests==2.28.0
six==1.16.0
SQLAlchemy==1.4.37
urllib3==1.26.9

-------------------------

El archivo settings.ini contiene la configuracion de la base de datos, en caso de querer cambiar la configuracion de la misma se deberan cambiar los parametros desde dicho archivo

-------------------------
Se deja adjunto un archivo SQL con el codigo para la creación de la base de datos, aqui se deja igualmente los comandos requeridos para esto.



---------------------- SQL PARA LA CREACION DE LA BASE DE DATOS---------
CREATE DATABASE challenge1;
CREATE USER u_challenge1 WITH PASSWORD 'password_challenge1';
GRANT ALL PRIVILEGES ON DATABASE "challenge1" to u_challenge1;




CREATE USER u_challenge1 WITH PASSWORD 'password_challenge1';
GRANT ALL PRIVILEGES ON DATABASE "challenge1" to u_challenge1;

