
-------- Creamos nueva Tabla: --------
create table Salarios (ID_empleado int,Apellido varchar(15),Nombre varchar(15),Seccional varchar(20), Facultad varchar(20),
Cargo varchar(20), Salario float,Fecha_comienzo date, Fecha_nacimiento date)

select *
from Salarios
--Le agregamos los datos Respectivos
/* 1°) forma ya la vimos*/

/* 2°) corresponde a la forma insertando los datos en todos los campos*/
 --insert into Salarios
 --select 

/* 3°) corresponde a la forma insertando campos especifícos*/
 
 -------- insert into Salarios(ID_empleado, apellido) values(dato_campo_ID:empleado, dato_campo:apellido) --------
 
 /*Ejercicio: insertar el siguiente registro:
 Nombre: Pedro Perez
 ID_empleado: 123456
 Seccional: Santiago
 Facultad: Docente
 Salario: 520000
 Fecha_comienzo: 28-08-2019
 Fecha_nacimiento: 01-01-2000 
 */
 
 select *
 from Salarios
 where ID_empleado = 123456
 
 -------- DELETE DE REGISTROS --------
 /* Una vez teniendo claro como filtrar en una tabla, podemos eliminar de la misma forma utilizando el comando delete: */
 /* LA FORMA DE UTILIZAR ESTE COMANDO ES:
	
	DELETE NOMBRE_TABLA
	WHERE [CONDICIONES]
*/
delete Salarios
where ID_empleado = 123456

-------- ACTUALIZACION DE REGISTROS EN UNA TABLA (UPDATE) --------
/* La sintaxis utilizada para actualizar un registro es similiar a hacer un filtro o eliminar:

UPDATE NOMBRE_TABLA
SET Campo_para_actualizar = Valor_nuevo
WHERE [CONDICIONES]
*/
UPDATE Salarios
set Nombre = 'Silvia'
where ID_empleado = 1011

/* se pueden actualizar simultaneamente varios campos para un mismo registro(o varios) siempre y cuando las condiciones se cumplan */

UPDATE Salarios
set Nombre = 'Silvia'
, Apellido = 'Gonzalez'
where ID_empleado = 1011

/* Ejecicio: La persona con el ID_empleado : 1153, paso a otro cargo: Docente*/


-------- INSTRUCCIÓN DISTINCT --------
/* Hacer un select con la opción distinct nos permite hacer una consulta, donde obtendremos el campo o los campos que
 necesitemos de manera unica, la forma de utilizar esta instrucción es:
 
 SELECT DISTINCT Campo(s)_requeridos
 from NOMBRE_TABLA
 */

/* Quiero saber todos los nombres que hay en la tabla */


-------- INSTRUCCIÓN TRUNCATE DE TABLE ----------
/* A veces cuando necesitemos borrar una tabla rapidamente, sin alterar su arquitectura, es decir solo borrar la información
que posee la Tabla, podemos utilizar la instrucción TRUNCATE, la forma de utilizarla es:

TRUNCATE TABLE NOMBRE_TABLA */

/******************** MUCHA PRECAUCIÓN, CUANDO SEA USADO ESTE COMANDO ************************/

/* EJERCICIO: BORRAR TODOS LOS DATOS DE LA TABLA Salarios */


/* nueva carga de datos: solo con código */

---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
-------------------------------- INSTRUCCION DROP TABLE --------------------------------
/* Caundo nos equivocamos creado una tabla, y simplemente queremos borrarla, usamos el comando DROP TABLE, de la siguiente forma:

DROP TABLE NOMBRE_TABLA
*/

/***************-------------------- PELIGRO CON ESTA INSTRUCCIÓN ----------------------********************/
/* EJERCICIO: ELIMINAR LA TABLA Monedas */


---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------
--------------------------------------------- OPERATORIA DE TABLAS ------------------------------------------------------
/* Cuando consultamos las tablas, normalmente no nos interesara solo hacer un select de la información propiamente tal como
sino que tambien queremos realziar calculos con ella. Para ello SQL provee que de forma simple uno puede operar tablas entre si
o por factores externos para poder calcular lo que necesitemos.*/

/*EJ: Para los datos de la tabla Salario, a todos le suben el sueldo al doble, como podemos ver eso */

/* Tambien a su vez, podemos crear nuevas columnas a partir de las existentes*/
/* EJ: Todos deben pagar un 20% de su salario como impuesto total, entonces como puedo ver entonces, el ingreso real
de cada trabajador */





--------------------------------------------- FILTRO COMODÍN: LIKE -------------------------------------------------------
/* Cuando filtramos en una tabla por uno o mas campos y los datos que necesito los puedo de alguna forma agrupar o encontrar algun patron
entonces me combiene utilizar like, veremos algunos ejemplos:*/

/*filtro por inicio de letra*/

/*filtro por %*/


/*filtro por contiene o no contiene*/


/*filtro por caracter*/










