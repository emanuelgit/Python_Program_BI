# -*- coding: utf-8 -*-



if __name__ == '__main__':
    condicion = True
    while(condicion):
        z = int(input("dime un numero:  "))
        if z % 2 == 0:
            print('tu numero es par\n')
        elif (z % 2 ==1) & (z >=0):
            print('tu numero es impar\n')
        elif z == -1:
            print('te aburriste de preguntar\n') 
            condicion = False
        else:
            print('Tu numero no es nada')
