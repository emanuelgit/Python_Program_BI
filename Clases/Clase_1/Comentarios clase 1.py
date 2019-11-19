# -*- coding: utf-8 -*-


# Funcion Dir
dir()
text_1 = 'hola'
text_2 = 'holasa'

text = 'hola'
Text = 'hola'
# help
# help(algo) Ctrl + i

# Función print

print('hola mundo')
print("hola mundo")
print('''hola mundo''')

print(''' este es un string largo
... y 'mas' largo aun
... y "super" largo''')

# Tipos de datos:
# String:
palabra = 'hola3456/(=)'
# funciones de los String
len(palabra)
palabra.zfill(20)
palabra.center(20)
palabra.split('a')

palabra = 'hola mundo; asdofsdgsdf'

# Números:
# a) Int:
num1 = 40
# se pueden soportar numeros muy grandes
num = 1234567890123456789012345678901234567890123456789012345678901234567890
print(num, num.bit_length(), sep=" :")
num = 123_123_123_123_23
print(num)
str(num).zfill(20)

# a) Float: hasta 16 digitos como maximo de precisión (desde el 17 se aproxima)
num = 123.123
#type(num)
print(type(num))
num = 1234.5678901234560

# Despues de la maxima precisión se escribe como notación cientifica.
num = 12345678901234567.8901234567890
print(num)

# equivalente a 1.23456789123456 x 10^100
num = 1.23456789012345678901234567890e+100
print(num)

# el mas grande número que se puede representar:
num = 1.7976931348623158e+308
print(num, end="\n\n")

# Sobrepasado el número mas grande se considera como infinito
num = 1.7976931348623159e+308
print(num)

# El número mas pequeño que se puede representar:
num = 5e-324
print(num)

# bajo el número mas pequeño es pasado a 0
num = 5e-325
print(num)

# podemos verificar si es entero o no
num = 123.123
print(num.is_integer())

num = 123.0
print(num.is_integer())

#%%
# listas (list):
lista = [1, 3, 4, 6]
print(lista)
size = len(lista)
print(size)

# Las listas pueden combinar varios tipos:
lista = [1, 1.0, 1+1j, True, 'YES', (1,2,3), [1,2,3]]
print(lista)
lista[6][0:2]

# Combinando listas
lista1 = [1, 2, 3, 4]
lista2 = ['A', 'B', 'C']
lista = lista1 + lista2
print(lista)
# listas multidimensionales
lista = [1, [4, 5, [6, 7]]]
print(lista)
lista[1][2][1]
# imprimiendo ciertos elementos
lista = [1, 2, 3, 4, 1, 1, 3, 3, 3, 3]
print(lista[2])
print(lista[-2])
print(lista[2:4])
print(lista[::2])
lista.append('a')
lista

la = []
la
for x in range(1,10):
    la.append(x)

for x in range(10):
    print(x)
la
la = list(range(1,10))
la
# otro ejemplo de lista multidimensional
lista = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

print(lista)
print(lista[2])
print(lista[-2][1])
print(lista[0][::2])
# Se pueden modificar los contenidos de las listas:
lista = [0,1, 2, 3, 4, 1, 1, 3, 3, 3, 3]
print(lista)
lista[0] = 10
print(lista)
lista[2:5] = [10, 20, 30, 40, 50]
print(lista)

#verificamos si se encuentra algún elemento:
print(50 in lista)
print(60 in lista)
lista.count(1)

#%%
# tuplas (tuple):
tupla = 1, 3, 4, 6  # herencia de Python 2.X
tupla = (1, 3, 4, 6)
print(tupla)
tupla = (1, 1.0, 1+1j, True, 'YES', (1,2,3))
print(tupla)
tupla = (1, (4, 5, (6, 7)))
print(tupla)
size = len(tupla)
print(size)
# Una tupla no puede ser modificada (no es mutable)
tupla = (1, 2, 3, 4, 1, 1, 3, 3, 3, 3)
tupla[0] = 10
# imprimimos ciertos elementos
print(tupla[2])
print(tupla[-2])
print(tupla[2:4])
print(tupla[::2])
# asignaciones mutiples
tupla = (1, 2, 3)
(a, b, c) = tupla

(a, b, c) = (1,2,3)
    
print(a,b,c,sep ='    ')
print(a,b,c,sep ='\t')
# Verificamos si algun elemento esta en la tupla:
print(1 in tupla)

#%%
# conjuntos (set):
cesta = {"pan", "vino", "queso", "carne", "pan"}
print(cesta)
print(dir(set))
# verificamos si un elemento esta en el set

lista = [0,1, 2, 3, 4, 1, 1, 3, 3, 3, 3]
set(lista)
tuple(lista)

tupla = (1, 2, 3)
list(tupla)
set(tupla)

print(cesta)
print('fruta' in cesta) 
cesta.add('fruta')
# no se puede
cesta[0]
print(cesta)
print('fruta' in cesta)

for w in cesta:
    cesta.pop()

cesta.pop()
for w in range(5):
    print(cesta.pop())

print(cesta)
# Extrae un elemento y lo saca de la lista
print(cesta.pop())
print(cesta)
# remueve el elemento pedido
cesta.remove('fruta') # Debe estar el elemento
print(cesta)
cesta.discard('fruta') # remueve solo si existe
vinos = set()  # creación conjunto vacío
a = set('abracadabra')
print(a)
b = set('alacazam')
print(b)
# letras en a pero no en b
print(a - b)
# letras en a o en b o en ambas 
print(a | b)
# letras en a y en b
print(a & b)
# letras en a o b pero no en ambos
print(a ^ b)

#%%
# Diccionarios (dict):
empleados = {1: "Pedro", 2: "Pablo", 3: "Juan"}  # crea diccionario empleados
print(empleados)
# agrega un elemento y actualiza otro
empleados.update({1: "Pedro Pablo", 4: "Ricardo"})
print(empleados)

print(sorted(empleados.keys()))
print(3 in empleados)
print("Ricardo" in empleados)

print(empleados[1])
print(empleados.pop(2))
print(empleados)
print()

# creación mediante secuencia
animales = dict([('perros', 4139), ('gatos', 4127), ('loros', 4098)])  
print(animales)  
print(animales['perros'])
animales['perros'] = 1234
print(animales['perros'])
print(animales.items())

for key in animales:
    print(str(key) + ":" + str(animales[key]))

for (key, val) in animales.items():
    print(str(key) + ":" + str(val))

for i, v in enumerate(sorted(animales.keys())):
    print("id: {0} nombre: {1} quantity: {2}".format(i, v, animales[v]))

# ultimo ejemplo
dicty = {x: x ** 2 for x in range(5)}
print(dicty)

#%%
# movernos entre listas, tuplas, sets, diccionarios


