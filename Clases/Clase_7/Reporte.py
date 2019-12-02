# -*- coding: utf-8 -*-

#%% Reporte
# 1) Buscamos las paridades: usd, eur
# 2) Las cargamos a nuestra base
# 3) Generamos la data que queremos en un data frame (opcional: puede ser con una
# vista)
# Actualizamos los datos de nuestro reporte a diario.
# Enviamos el mail respectivo con la información.

import os
os.chdir("C:\Program BI\Python ver 2.0\Clase 7")

from bs4 import BeautifulSoup as bs
import requests
import datetime as dt
import pyodbc
from win32com import client


def trae_paridades():    
    main_url = "https://www.bcentral.cl"
    req = requests.get(main_url)
    soup = bs(req.text, "html.parser")
    title = soup.find("div", class_ = "tab-pane active")    
    #len(lista)
    x = str(list(title)[1])  
    frase = 'Dólar Observado</td>\n<td>'
    pos_1 = x.find(frase)
    pos_2 = x[pos_1:].find('</td>\n</tr>')+pos_1
    new_x = x[pos_1:pos_2]
    pos_3 = new_x.find('<td>')
    usd = float(new_x[pos_3+4:].replace(',','.'))
    frase = 'Euro</td>\n<td>'
    pos_1 = x.find(frase)
    pos_2 = x[pos_1:].find('</td>\n</tr>\n<tr>')+pos_1
    new_x = x[pos_1:pos_2]
    pos_3 = new_x.find('\n<td>')
    eur = float(new_x[pos_3+5:].replace(',','.'))    
    return ([usd,eur])

def carga_sql_paridades_dia():
    [usd,eur] = trae_paridades()
    # conectamos con sql:
    hoy = dt.date.today()
    con = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-RP1INROE\SQLEXPRESS;'
                      'Database=SQL;'
                      'Trusted_Connection=yes;')
    cursor_escritura = con.cursor()
    sql = "delete Monedas where fecha = '" + str(hoy) + "'"
    cursor_escritura.execute(sql)
    con.commit()
    # insertamos los dos valores:    
    # Dolar a CLP
    sql = "insert into Monedas select '%s','BCC','USD','CLP',%s" %(hoy,usd)
    cursor_escritura.execute(sql)
    # Euro a CLP
    sql = "insert into Monedas select '%s','BCC','EUR','CLP',%s" %(hoy,eur)
    cursor_escritura.execute(sql)
    con.commit()
    cursor_escritura.close()
    con.close()
    return([usd,eur])

import xlwings as xw
from win32com import client


def Completamos_informe():
    # Abre un workbook y retorna un objecto workbook de xlwings. 
    # Sin screen_updating es false es mas rapido.   
    wb = xw.Book('Reporte.xlsx')
	 if screen_updating == False:
         wb.app.screen_updating = False
	 else:
         wb.app.screen_updating = True
	 if visible == False:
         wb.app.visible = False
	 else:
         wb.app.visible = True
    # limpiamos la hoja donde pegaremos los datos:
    wb.sheets["Data"].clear_contents()
	 # abrimos la conexión con sql para traer la data:
    con = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-RP1INROE\SQLEXPRESS;'
                      'Database=SQL;'
                      'Trusted_Connection=yes;')    
    sql = "select * from Ventas_final"
    data = pd.read_sql(sql,con)
    cabezales = list(data.columns)
#    pegar_valor_celda(wb, "Data", 1, 1, cabezales)
#    pegar_valor_celda(wb, "Data", 1+1, 1, data[:,:])
    
    pegar_valor_celda(wb, "Data", 1, 1, data.iloc[:,0:].values)
    wb.save()
    wb.close()
       
    
    # funcion para insertar en una celda especifica un valor:
    def pegar_valor_celda(wb, sheet, row, column,value):
        wb.sheets[sheet].range(row,column).value = value
    

        
        
    
    
    
    
    
    
    
    
#app = wb.app
#	 app.quit()
#    
#    sheet_index = wb.sheets['Data'].index    
#    xlApp = client.Dispatch("Excel.Application")
#	 books = xlApp.Workbooks(1)
#	 ws = books.Worksheets[sheet_index]
#	 ws.ExportAsFixedFormat(0, path_out)    
    
    
    
    
    
    
    
    



