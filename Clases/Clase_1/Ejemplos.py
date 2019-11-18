# -*- coding: utf-8 -*-

# Ejemplo 1:
# lecturas de archivos:
import pandas as pd
urldata = 'https://raw.githubusercontent.com/emanuelgit/Python_Program_BI/master/data/titanic/titanic3.csv'
data = pd.read_csv(urldata)

# Ejemplo 2:
# Impresion en consola:
text = 'Curso\n\tPython' # \n print an ENTER
print(text)

# Ejemplo 3:
# Datos de entrada
name = input("Name    : ")
surname = input("Surname : ")
edad = input("edad:")
print("Thanks,", name, surname)
print("Thanks,{0} {1} de {2} años ".format(name,surname,edad))
#print("Thanks,\n{0}\n{1}\nde {2} años ".format(name, surname,edad))

# Ejemplo 4:
# Imprimiendo el hola mundo
text1 = "Hola"
text2 = "Mundo"
text = text1 + " " + text2
print(text)

text = "My name is %s %s and I'm %d years old"
formated_text = text % ("Juan", "Perez", 20)
print(formated_text)

# GRAFICOS 1

import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib
# %matplotlib inline
x = np.linspace(-1, 1, 100)
y = x ** 2
plt.plot(x, y)
plt.show()

# GRAFICOS 2
import numpy as np
import matplotlib.pyplot as plt
# pip install matplotlib
x = np.linspace(-1, 1, 100)
for n in range(1, 10):
    y = x ** n
    plt.plot(x, y, label='x^{}'.format(n))

plt.xlabel('Value')
plt.ylabel('Result Value')
plt.title('Values Graph')
plt.grid(True)
plt.legend()
plt.show()

data.to_excel("data_web.xlsx")



