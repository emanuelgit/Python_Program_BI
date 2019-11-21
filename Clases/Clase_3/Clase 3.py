# -*- coding: utf-8 -*-
import os
os.chdir('C:\Program BI\Python ver 2.0\Clase 3')

import pandas as pd
import datetime as dt
# Data Frames
# Acceder a datos del DataFrame
ventas = pd.read_excel('Ventas.xlsx')
ventas = pd.read_excel('Ventas.xlsx',index_col = 'Fecha')
ventas.dtypes
# tenemos el loc y iloc:
ventas.iloc[0,0]
ventas.iloc[0,3]
ventas.iloc[:,0]
ventas.iloc[1,:]

ventas.loc[0,'Cantidad']
ventas.index

ventas = pd.read_excel('Ventas.xlsx',index_col = 'Fecha')


# Crear Data Frames a partir de diccionarios:
dic = {'nombre': ['juan','pedro','diego'], 'edad': [19,23,26], 
       'telefono':[1234,34534,12312]}
df_dic = pd.DataFrame(dic)
df_dic = pd.DataFrame(dic,index = list(dic['nombre']))

# Crear Data Frame vacíos:
import numpy as np
np.ones(10)
np.ones((5,5))
np.zeros((3,3))
df_zero = pd.DataFrame(np.zeros((3,3)), columns = ['nombre', 'edad','telefono'])
df_zero.loc[:,'nombre'] = dic['nombre']
df_zero.loc[:,'edad'] = dic['edad']
df_zero.loc[:,'telefono'] = dic['telefono']
df_zero.index = df_zero['nombre']
df_zero.drop(columns=['nombre'],inplace=True)

# Unir Data Frames:
df_dic_2 = pd.DataFrame({'nombre':['pablo','jose'],'edad': [32,45],
                         'telefono': [1234,2234]}, index = ['pablo','jose'])
df_dic
df_dic.drop(columns=['nombre'],inplace=True)
df_dic_2.drop(columns=['nombre'],inplace=True)
pd_dic_T = pd.concat([df_dic,df_dic_2])

pd_dic_T.to_excel('ejemplo_amigos.xlsx')

# Trabajaremos con archivos:


# Leer la serie de precios de activos
df = pd.read_excel('serie.xlsx')
# llenar los nan con 0's
df.fillna(0)
# llenar con el valor anterior encontrado
df_2 = df.fillna(method='ffill')

# llenar con el valor despues encontrado
df_2 = df.fillna(method='backfill')

# llenar con el valor despues encontrado
df_2 = df.fillna(method='Interp')

df_2 = df.interpolate(method='linear',axis=0,inplace=True)
# Lectura  de las ventas
# Ver gráficos
import matplotlib.pyplot as plt
ventas = pd.read_excel('Ventas.xlsx')
plt.hist('Cantidad',data = ventas)
plt.plot('Fecha','Cantidad',label='Cantidad',data = ventas)
# las libreria matplotlib le agrega funcionalidades a la libreria pandas
ventas.plot('Fecha','Cantidad')
ventas.plot('Fecha','Cantidad',title = 'cantidad vendida')
ventas.hist('Cantidad')
plt.savefig('grafico.jpeg')
# Calcular beneficio
# beneficio = (ventas - costos)

# Verificar si tendra bono (utilidades sobre costo > 10%)
