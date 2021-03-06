
-- CREACIÓN DE TABLAS --
-- Información de ventas --
create table Ventas (Fecha date not null, Cantidad int,Ventas float, costos float)

/*drop table Ventas*/

-- Información de Paridades --
create table Monedas(Fecha date, Fuente varchar(5),Moneda_Numerador varchar(3),
 Moneda_Denominador varchar(3),Valor float)

select *
from Monedas


-- Consultas: ---
/* Select Simple */
select *
from Monedas

select Fecha,Fuente,Moneda_Numerador,Moneda_Denominador,Valor
from Monedas

select *
from Ventas

select Fecha,Cantidad,costos,ventas,utilidad = Ventas - costos 
from Ventas

--truncate table Ventas

select *,utilidad = Ventas - costos 
into ventas_utilidad
from Ventas

--drop table ventas_utilidad

select Fecha,Cantidad,costos,ventas,utilidad = Ventas - costos, factor = ((Ventas - costos)/costos)*100
into ventas_utilidad_2
from Ventas

select Fecha,Cantidad,costos,ingresos= ventas
from ventas

/* FILTROS:
Los filtros en la instrucción WHERE son condiciones que les ponemos a las columnas que posee la tabla, de tal manera de que los
registros que obtengamos, sean solo los que necesitamos
*/

---------------------------------------------------------------------------------------------------
/* La forma de poner el filtro es con una condición de verdad que se cumpla*/

-- Filtro de igualdad (=):
select *
from Monedas
where fecha = '20190106'

select *
from Ventas
where fecha = '2018-12-26'

select *
from Ventas
where fecha = '20180228'



-- Filtro de desigualdad (<>):
select *
from Ventas
where fecha <> '20190106'

-- Filtro de estar en un conjunto de datos (in):
select *
from Monedas
where Moneda_Denominador in ('USD','JPY')

-- Filtro de no estar en un conjunto de datos (not in):

select *
from Monedas
where Moneda_Denominador not in ('CLF','CAD')

-- Filtros de Opciones "Y" y "O":
-- Y (and):
select *
from Monedas
where fecha = '20190801' and Moneda_Denominador = 'CLP'

-- O (or):
select *
into tabla_filtrada
from Monedas
where Moneda_Numerador = 'AUD' or Moneda_Numerador = 'BRL'

insert into tabla_filtrada
select *
from Monedas
where Moneda_Numerador = 'USD'

--delete [nombre_tabla]
--where condiciones

select *
from tabla_filtrada
where Moneda_Denominador = 'BRL'

delete tabla_filtrada
where Moneda_Denominador = 'BRL'
[tabla filtrada]
-- truncate table 

-- Combinación:
select *
from Monedas
where (Moneda_Numerador = 'AUD' or Moneda_Numerador = 'BRL') and Fecha = '20190801'

-- De igualdades o desigualdades numericas:

select *
from Monedas
where Moneda_Numerador = 'USD' and Moneda_Denominador = 'CLP' and Valor <=700

select *
from Monedas

-- Insertar datos a la tabla:
insert into Monedas select '20191126','BBG','USD','CLP',789.89

insert into Monedas(Fecha,Fuente,Moneda_Numerador,Moneda_Denominador,Valor) values('20191126','BBG','USD','CLP',789.89)

insert into Monedas(Fecha,Fuente,Moneda_Numerador,Moneda_Denominador,Valor) 
values('20191127','BBG','USD','CLP',790.89)

insert into Monedas(Fecha,Moneda_Numerador,Moneda_Denominador,Valor) 
values('20191128','USD','CLP',791.89)

-- Comando Truncate es para eliminar todos los datos de una tabla sin eliminar la arquitectura de la tabla
truncate table Monedas

select *
from Monedas

insert into Monedas(Fecha,Fuente) values('20191129','BBG')

select *
from Monedas
where Moneda_Numerador is null

select *
from Monedas
where Moneda_Numerador is null


select Fecha,Fuente,Moneda_Numerador = case when Moneda_Numerador is null then 'CLP' end,
Moneda_Denominador,Valor
from Monedas
where Moneda_Numerador is null

select Fecha,Fuente,isnull(Moneda_Numerador,'CLP'),
Moneda_Denominador,Valor
from Monedas
where Moneda_Numerador is null

update Monedas
set Moneda_Numerador = 'CLP'
where Moneda_Numerador is null 

select Fecha,Fuente,Moneda_Numerador,
Moneda_Denominador = case when Valor is null then 0
						  when Valor <0 then -100
						  when Valor >0 then 100
						  end
from Monedas
where Moneda_Denominador is null



select *,bono = case when ((ventas -costos)/costos)>0.1 then 1 else 0 end
from ventas

select *, recibe_bono= case when bono = 1 then 'Se gano el bono' else 'siga participando' end
from 
(select *,bono = case when ((ventas -costos)/costos)>0.1 then 1 else 0 end
from ventas) as A


select SUM(ventas)
from ventas


select Fecha,SUM(ventas)
from ventas
group by Fecha

select Fecha,SUM(ventas)
from ventas
group by Fecha
order by Fecha desc

select month(Fecha),SUM(ventas)
from ventas
group by month(Fecha)

select Fecha,SUM(ventas)
from ventas
where Fecha between '20190101' and '20190625' 
group by Fecha


select Fecha,Cantidad
from ventas
where cantidad between 90 and 100


