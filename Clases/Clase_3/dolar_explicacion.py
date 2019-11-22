# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
import requests
import datetime as dt

# Obtenemos el Dolar del Banco Central
main_url = "https://www.bcentral.cl"
req = requests.get(main_url)
soup = bs(req.text, "html.parser")
str(soup)

title = soup.find("div", class_ = "tab-pane active")
str(title)
palabra = 'hola'
palabra.find('a')

lista = list(title)
#len(lista)
list(title)[0]
list(title)[1]
list(title)[2]

x = str(list(title)[1])
  
frase = 'Dólar Observado</td>\n<td>'
pos_1 = x.find(frase)

x[pos_1:]
#word = x[pos_1:]
pos_2 = x[pos_1:].find('</td>\n</tr>')+pos_1
new_x = x[pos_1:pos_2]
pos_3 = new_x.find('<td>')
valor = float(new_x[pos_3+4:].replace(',','.'))

#%% Otra Mirada
frase_corta_1 = x[pos_1:]
pos_2 = frase_corta_1.find('</td>\n</tr>')
frase_corta_3 = frase_corta_1[:pos_2]
pos_3 = frase_corta_3.find('<td>')
float(frase_corta_3[pos_3+4:].replace(',','.'))









