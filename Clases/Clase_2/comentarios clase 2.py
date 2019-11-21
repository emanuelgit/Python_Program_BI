# -*- coding: utf-8 -*-

# Dejar los valores desde el 1 al 100 en una lista

x = 1
lista = []
while(x<=100):
    lista.append(x)    
    x += 1 # x = x+1
print(lista)

lista_2 = []
for x in range(1,101):
    lista_2.append(x)

print(lista_2)

lista_3 = list(range(1,101))
print(lista_3)

# generar una lista del 0 al 100 solo con números pares:

print(list(range(0,101,2)))

#for 
a = 5
b = 2
a%b


lista_4 = []
for x in range(0,101):
    if x%2 == 0:
        lista_4.append(x)

print(lista_4)
    
    
z = 9
if z == 8:
    print('es 8')
elif z == 11:
    print('holasd')
elif z == 12:
    print('hsdasolasd')    
else:
    print('es un numero distinto de 8') # palabra reservada pass: para que continue con el codigo


# Pide un número por teclado y guarda en una lista su tabla de 
# multiplicar desde el 1 hasta el 100. 
# por ejemplo si pide el 2 la lista tendrá: 
# [2,4,6,8,10,12,14,16,18,20,..200]

lista = []

num1 = int(input('Dame un valor: '))

for x in range(1,101):
    lista.append(x*num1)
    
print(lista)

#%% tarea 3

lista_5 = []
contador = 1
while(contador < 11):
    num = int(input('Dame un valor: '))
    lista_5.append(num)
    contador +=1
lista_5.sort()
print(lista_5)



lista_6 = []
contador = 1
while(True):
    num = int(input('Dame el numero ' + str(contador) + ':'))
    lista_6.append(num)
    contador +=1
    if contador == 11:
        break
lista_6.sort()
print(lista_6)



# diccionarios
telefonos = {'juan':8909, 'pedro':1123}
print(telefonos)
list(telefonos)


print(list(zip(range(1,10),range(9))))

l_1 = ['z','b','c']
l_2 = [1,2,3]

print(list(zip(l_1,l_2)))

print(list(zip(l_1,l_2,range(2))))

#%% funciones

def mi_primera_funcion(x,y):
    return(x+y)

mi_primera_funcion(4,5)
mi_primera_funcion(-2,5)

# crear una funcion que necesite 3 parametros y devuelva la multiplicacion
# de los 3 numeros


def funcion_mul(x,y,z):
    return(x*y*z)

def funcion_mul_2(x,y,z):
    print(x*y*z)

m = funcion_mul(2,3,4)
m2 = funcion_mul_2(2,3,4)


import datetime as dt
def mi_segunda_function():
    return dt.date.today()

print(mi_segunda_function())

def mi_tercera_function():
    return dt.datetime.today()

print(mi_tercera_function())



funcion_corta = lambda n: (n*100)
funcion_corta(5)

funcion_corta_2 = lambda x,y: ((x+y)*100)
funcion_corta_2(2,3)

funcion_corta_3 = lambda x: list(range(x))
funcion_corta_3(8)


[(x,y) for x in range(9) for y in range(-2,7)]

[(x,y) for x,y in zip(range(9),range(-2,7))]


[(x,y) for x in range(9) for y in range(-2,7) if x == 2*y]

[x/x for x in range(1,11) ]







