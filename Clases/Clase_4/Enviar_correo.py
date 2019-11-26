# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:49:13 2019

@author: Emanuel&Mara
"""
from win32com import client
import pandas as pd
import datetime as dt

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
    if attachment_paths:
        for att in attachment_paths:
            newMail.Attachments.Add(Source=att)
    try:
        newMail.Send()
        print("Correo enviado")
    except:
        print("Fallo en el envío del correo")
        
        
#if __name__ == '__main__':
#    enviar_mail()  