# -*- coding: utf-8 -*-
import os
os.chdir('C:/Program BI/Python ver 2.0/Clase 5')


import pandas as pd
import datetime as dt


df = pd.read_excel('test_1.xlsx')
df.describe()

dic = {'nombre': ['juan','pedro','diego'], 'edad': [19,23,26], 
       'telefono':[1234,34534,12312]}
df_dic = pd.DataFrame(dic)
df_dic = pd.DataFrame(dic,index = list(dic['nombre']))

# Unir Data Frames:
df_dic_2 = pd.DataFrame({'nombre':['pablo','jose'],'edad': [32,45],
                         'telefono': [1234,2234]}, index = ['pablo','jose'])

df_dic.drop(columns=['nombre'],inplace=True)
df_dic_2.drop(columns=['nombre'],inplace=True)
pd_dic_T = pd.concat([df_dic,df_dic_2])

df_dic_3 = pd.DataFrame({'comuna': ['santiago','florida'],
                         'estado_civil' : ['casado','soltero']}, index = ['pablo','jose'])

pd_dic_T_2 = pd.concat([df_dic_2,df_dic_3],axis = 1)

pd_dic_T.dtypes

pd_dic_T.to_excel('ejemplo_amigos.xlsx')

pd_dic_T.to_csv('amigos.txt',sep=';')

# Trabajaremos con archivos:

# Leer la serie de precios de activos
df = pd.read_excel('serie.xlsx')
# llenar los nan con 0's
df.fillna(0,inplace = True)
# llenar con el valor anterior encontrado
df_2 = df.fillna(method='ffill')

# llenar con el valor despues encontrado
df_2 = df.fillna(method='backfill')

df_3 = df_2.fillna(method='ffill')

# llenar con el valor interpolado
#df_2 = df.fillna(method='Interp')

df_2 = df.interpolate(method='linear',axis=0)
df_3 = df_2.interpolate(method='linear',axis=1)

nulos = df_2.isna()
nulos_2 = df_2.isna().isna()

#%%
valor = "CERDE\u00c3\u0091A"
print(valor)
print('\u00c3')
print('\u0091')
print('\\')

#%%
# Lectura  de las ventas
# Ver gráficos
import pandas as pd
import matplotlib.pyplot as plt
ventas = pd.read_excel('Ventas.xlsx')
plt.hist('Cantidad',data = ventas)

plt.hist('Cantidad',data = ventas)
ventas.index = ventas['Fecha']
plt.hist('Cantidad',data = ventas)

plt.hist(ventas['Cantidad'])

plt.plot('Fecha','Cantidad',label='Cantidad',data = ventas)
plt.plot('Fecha','Cantidad','bo',data = ventas)
plt.plot('Fecha','Cantidad','r+',data = ventas)
plt.plot('Fecha','Cantidad','go--',data = ventas)

# las libreria matplotlib le agrega funcionalidades a la libreria pandas

ventas.plot('Fecha','Cantidad')
ventas.plot('Fecha','Cantidad',title = 'cantidad vendida')
ventas.boxplot('Ventas(MM$)')

ventas.hist('Cantidad')
plt.savefig('grafico.pdf')
# Calcular beneficio
# beneficio = (ventas - costos)
ventas
# Verificar si tendra bono (utilidades sobre costo > 10%)

#ventas['cantidad/100'] = ventas['Cantidad']/100

ventas['Beneficio'] = ventas['Ventas(MM$)'] - ventas['Costos(MM$)']
ventas['Beneficio'] = ventas.loc[:,'Ventas(MM$)'] - ventas.loc[:,'Costos(MM$)']
ventas['Beneficio'] = ventas.iloc[:,2] - ventas.iloc[:,3]


# si ventas['Beneficio']/ventas['Costos(MM$)'] > 0,1 entonces 1, sino 0
#def recibe_bono(beneficio_costo):    
#    if beneficio_costo > 0.1:
#        return(1)
#    else:
#        return(0)
 
#if corto           
z = 8
'si es 8' if z==8 else 'es otro numero'

1 if z==8 else 0
ventas.isnull().all(axis=0)
ventas.isempty
ventas.any()

# con False o True
ventas['Bono'] = (ventas['Beneficio']/ventas['Costos(MM$)'] >0.1)
# es un tema bien delicado trabajar con valores de verdad en los data frame, 
# se puede generar ambigüedad
ventas['Bono'] = [1 if x>0.1 else 0 for x in (ventas['Beneficio']/ventas['Costos(MM$)'])]

# FILTROS
ventas['Fecha'][ventas['Bono'] == 1]

ventas['Fecha'][(ventas['Bono'] == 1) & (ventas['Cantidad'] > 90)]

ventas['Fecha'][(ventas['Bono'] == 1) | (ventas['Cantidad'] > 90)]
# Filtrar por varias columnas
ventas[['Fecha','Cantidad']][(ventas['Bono'] == 1) | (ventas['Cantidad'] > 90)]

bono = lambda x: 1 if (x > 0.1) else 0



(ventas['Beneficio']/ventas['Costos(MM$)']).apply(lambda x: 1 if x>0.1 else 0)


