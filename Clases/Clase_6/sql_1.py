# -*- coding: utf-8 -*-

import pyodbc
import pandas as pd
con = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-RP1INROE\SQLEXPRESS;'
                      'Database=SQL;'
                      'Trusted_Connection=yes;')


# %% Lectura de Datos de la tabla monedas
df_monedas = pd.read_sql('select * from Monedas',con)
df_ventas = pd.read_sql('select * from ventas',con)


# %% Insertando datos en la tabla Monedas
df = pd.read_excel('Monedas.xlsx')
cursor = con.cursor()
for i in df.index:
    valores = tuple(df.loc[i,:])
    sql = "insert into Monedas select '%s','%s','%s','%s',%s" %(valores)
    cursor.execute(sql)
con.commit()    

cursor.close()
con.close()
