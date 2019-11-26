# -*- coding: utf-8 -*-

from win32com import client
import pandas as pd
import datetime as dt
import os
from bs4 import BeautifulSoup as bs
import requests
import openpyxl
#os.chdir('C:\Program BI\Python ver 2.0')
basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

def enviar_mail(subject, body, mails, attachment_paths=None):    
    olMailItem = 0x0
    obj = client.gencache.EnsureDispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = subject    
    cadena = ""
    for mail in mails:
        mail = mail+";"
        cadena = cadena+mail
    cadena=cadena[:-1] # los mails se mandan separados por ; en una cadena
    newMail.To = cadena
    #newMail.CC = cadena
    #newMail.CCO = cadena
    newMail.BCC = 'moliva@programbi.cl'
    if attachment_paths:
        for att in attachment_paths:
            newMail.Attachments.Add(Source=att)
    try:
        newMail.Send()
        print("Correo enviado")
    except:
        print("Fallo en el envío del correo")
        

mails = pd.read_excel('lista_mail.xlsx')

mails.index
path = 'C:/Program BI/Python ver 2.0/Clase 4/'
for i in mails.index:    
    print(mails.loc[i].values)
    enviar_mail('Asunto importante n°: ' +str(i),
                'Estimado, le escribo por el asunto: ' + str(i*100),
                mails.loc[i].values,
                [path + 'Dolar.xlsx',
                 path + 'grafico.jpeg'])
    #print(mails.loc[i,'Lista de Mail'])
    #print(mails.iloc[i,0])
    
    
    
    
    
    
    
    
    
    



        