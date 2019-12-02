# -*- coding: utf-8 -*-

import os
os.chdir("C:\Program BI\Python ver 2.0\Clase 7")
# A cargar:

# bajamos dolar, euro

# lo ingresamos a una tabla (sql) y un nuevo registro

# calculamos lo necesario en ventas en SQL
# Exportamos a pdf

# Finalmente guardamos la data de como va la cosa en un excel y se envía por
# correo (se actualiza la data)



# 1) cargamos la data SQL
# Ventas_comercial
import pyodbc
import pandas as pd
con = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-RP1INROE\SQLEXPRESS;'
                      'Database=SQL;'
                      'Trusted_Connection=yes;')
df = pd.read_excel('Ventas_comercial.xlsx')
cursor_escritura = con.cursor()
sql = "truncate table Ventas_comercial"
cursor_escritura.execute(sql)
con.commit()
for i in df.index:
    valores = tuple(df.loc[i,:])    
    sql = "insert into Ventas_comercial select '%s','%s','%s','%s','%s'" %(valores)
    cursor_escritura.execute(sql)
con.commit()

# Monedas
df = pd.read_excel('Monedas.xlsx',sheet_name = "Monedas" )
# Opcional, podemos hacer el truncate desde acá:
sql = "truncate table Monedas"
cursor_escritura.execute(sql)
con.commit()
for i in df.index:
    valores = tuple(df.loc[i,:])    
    sql = "insert into Monedas select '%s','%s','%s','%s',%s" %(valores)
    cursor_escritura.execute(sql)
con.commit()
cursor_escritura.close()
con.close()

# Con la data necesaria cargada, podemos hacer el reporte de manera diaria.



