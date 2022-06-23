ir al directorio donde se vaya a crear el entorno virtual para la app

virtualenv challenge1

cd directorio_virtual/challenge1/Scripts/
./activate

pip install SQLAlchemy and pip install psycopg2
pip install requests
pip install pandas

Error de conexion ssl para la descarga de archivos csv con request

---- estos pasos se siguieron se resolvio el problema, copiar archivos dll de bin a dll-----
https://github.com/conda/conda/issues/8273
---------------------------------------------------------------





CREATE DATABASE challenge1;
CREATE USER u_challenge1 WITH PASSWORD 'password_challenge1';
GRANT ALL PRIVILEGES ON DATABASE "challenge1" to u_challenge1;

















create or replace function limpiar_tabla(_tbl regclass,out result integer) 
	language plpgsql as 
$func$
begin

	execute format('delete from %s where true' ,_tbl);

--	delete from  public.b;

	end;
$func$;

select limpiar_tabla('public."T_Agrupados"');
