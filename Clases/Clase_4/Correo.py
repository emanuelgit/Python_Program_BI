# -*- coding: utf-8 -*-


import win32com.client

def send_mail_via_com(text, subject, recipient, profilename="Outlook2013"):
    s = win32com.client.Dispatch("Mapi.Session")
    o = win32com.client.Dispatch("Outlook.Application")
    s.Logon(profilename)

    Msg = o.CreateItem(0)
    Msg.To = recipient

    Msg.CC = "emanuel.berrocal@gmail.com"
    #Msg.BCC = "address"

    Msg.Subject = subject
    Msg.Body = text

    attachment1 = "Dolar.xlsx"
    #attachment2 = "Path to attachment no. 2"
    Msg.Attachments.Add(attachment1)
    #Msg.Attachments.Add(attachment2)

    Msg.Send()

send_mail_via_com('hola amigos', 
                  'test', 'emanuel.berrocal@gmail.com')    