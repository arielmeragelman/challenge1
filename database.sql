CREATE DATABASE challenge1;
CREATE USER u_challenge1 WITH PASSWORD 'password_challenge1';
GRANT ALL PRIVILEGES ON DATABASE "challenge1" to u_challenge1;




CREATE USER u_challenge1 WITH PASSWORD 'password_challenge1';
GRANT ALL PRIVILEGES ON DATABASE "challenge1" to u_challenge1;


CREATE TABLE public."T_Agrupados" (
	"index" int8 NULL,
	"Cod_Loc" int8 NULL,
	"IdProvincia" int8 NULL,
	"IdDepartamento" int8 NULL,
	categoria text NULL,
	provincia text NULL,
	localidad text NULL,
	nombre text NULL,
	direccion text NULL,
	"CP" text NULL,
	telefono text NULL,
	mail text NULL,
	web text NULL,
	modifica float8 NULL
);
CREATE INDEX "ix_public_T_Agrupados_index" ON public."T_Agrupados" USING btree (index);



CREATE TABLE public."T_Cines" (
	"index" int8 NULL,
	"('provincia', '')" text NULL,
	"('Pantallas', 'sum')" int8 NULL,
	"('Butacas', 'sum')" int8 NULL,
	"('espacio_INCAA', 'sum')" int8 NULL
);
CREATE INDEX "ix_public_T_Cines_index" ON public."T_Cines" USING btree (index);


CREATE TABLE public."T_Total" (
	"index" text NULL,
	"0" int8 NULL
);
CREATE INDEX "ix_public_T_Total_index" ON public."T_Total" USING btree (index);


create or replace function limpiar_tabla(_tbl regclass,out result integer) 
	language plpgsql as 
$func$
begin

	execute format('delete from %s where true' ,_tbl);

--	delete from  public.b;

	end;
$func$;




