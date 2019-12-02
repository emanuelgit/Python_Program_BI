

create table Ventas_comercial(Fecha smalldatetime,Cantidad int,Ventas float,Costos float,
Moneda varchar(3), primary key(Fecha))


select *
from Ventas_comercial

select *
from Monedas


select A.Fecha,A.Cantidad,
A.Ventas,A.Costos,A.Moneda,
Venta_total = case when A.Moneda = 'CLP' then A.Ventas
				   when A.Moneda = 'EUR' then A.Ventas*B.Valor
				   when A.Moneda = 'USD' then A.Ventas*B.Valor
				   end
from Ventas_comercial as A left join Monedas as B on
(A.Fecha = B.Fecha and A.Moneda = B.Moneda_Numerador and B.Moneda_Denominador = 'CLP')


create view Ventas_final
as
select A.Fecha,A.Cantidad,
A.Ventas,A.Costos,A.Moneda,
Venta_total = case when A.Moneda = 'CLP' then A.Ventas
				   when A.Moneda = 'EUR' then A.Ventas*B.Valor
				   when A.Moneda = 'USD' then A.Ventas*B.Valor
				   end
from Ventas_comercial as A left join Monedas as B on
(A.Fecha = B.Fecha and A.Moneda = B.Moneda_Numerador and B.Moneda_Denominador = 'CLP')


-- resumen por mes para las ventas:

select mes = MONTH(fecha),Cantidad_total = sum(Cantidad),Total_venta = sum(Venta_total),
Total_costos = sum(Costos), Promedio_por_mes = AVG(Cantidad),sum(cantidad)/COUNT(cantidad)
from Ventas_final
group by MONTH(fecha)


select *
from Ventas_final