# -*- coding: utf-8 -*-

import Todo_junto as mt
import datetime as dt


if __name__ == '__main__':
    dolar_dia = mt.guada_dolar()
    fecha_hoy = dt.date.today()
    mt.enviar_mail('El dolar del día','El dolar del día: '+ fecha_hoy.strftime('%d-&m-%y') + ' fue: ' + str(dolar_dia),
                ['emanuel.berrocal@gmail.com','moliva@programbi.cl'],
                ['C:/Program BI/Python ver 2.0/Clase 4/Dolar.xlsx'])