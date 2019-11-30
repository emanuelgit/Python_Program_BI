# -*- coding: utf-8 -*-

import pyodbc
import pandas as pd
con = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-RP1INROE\SQLEXPRESS;'
                      'Database=SQL;'
                      'Trusted_Connection=yes;')

#con = pyodbc.connect('Driver={SQL Server};'
#                      'Server=LAPTOP-RP1INROE\SQLEXPRESS;'
#                      'uid= user'
#                      'pwd = clave'
#                      'Database=SQL;'
#                      'Trusted_Connection=no;')

# %% Lectura de Datos de la tabla monedas
df_monedas = pd.read_sql('select * from Monedas',con)
df_monedas.to_excel('monedas_sql.xlsx',index =False)

df_monedas_f_2 = pd.read_sql("select * from Monedas where Moneda_Denominador = 'CLP'",con)
df_monedas_f_2['Valor_doble'] = df_monedas_f_2['Valor']*2

df_ventas = pd.read_sql('select * from ventas',con)


# %% Insertando datos en la tabla Monedas
df = pd.read_excel('Monedas.xlsx')
cursor_escritura = con.cursor()

tuple(df.loc[0,:])

tuple(df.iloc[0,0:2])
x = 9
print('mi numero es %s, y \n despues crecio a %s' %(x,2*x))
print('mi numero es %s, y \n despues crecio a %s')
for i in df.index:
    valores = tuple(df.loc[i,:])
    #print(valores)
    sql = "insert into Monedas select '%s','%s','%s','%s',%s" %(valores)
    cursor_escritura.execute(sql)
con.commit()

cursor_escritura.close()
con.close()






