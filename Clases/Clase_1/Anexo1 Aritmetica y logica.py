# -*- coding: utf-8 -*-

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
print(''.center(50, '-'))
print('Suma'.ljust(20), ':', num1 + num2)
print('resta'.ljust(20), ':', num1 - num2)
print('Multiplicacion'.ljust(20), ':', num1 * num2)
print('Division'.ljust(20), ':', num1 / num2)
print('Division Entera'.ljust(20), ':', num1 // num2)
print('Modulo'.ljust(20), ':', num1 % num2)
print('Potencia'.ljust(20), ':', num1 ** num2)
print(''.center(50, '-'))
print('Modulo'.ljust(20), ':', num1 % num2, sep='\n')

# Otras formas:
# num1 = num1 + num2
num1 += num2
# num1 = num1 - num2
num1 -= num2
# num1 = num1 * num2
num1 *= num2
# num1 = num1 / num2
num1 /= num2
# num1 = num1 // num2
num1 //= num2
# num1 = num1 ** num2
num1 **= num2
# num1 = num1 % num2
num1 %= num2

# ---------------------- Comparaciones ------------------------------


print('Comparando Numeros'.center(50))
print(''.center(50, '-'))
num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
print(''.center(50, '-'))
print('Menor que'.ljust(25), ':', num1 < num2)
print('Menor o igual a'.ljust(25), ':', num1 <= num2)
print('Mayor a'.ljust(25), ':', num1 > num2)
print('Mayor o igual a'.ljust(25), ':', num1 >= num2)
print('Igual'.ljust(25), ':', num1 == num2)
print('distinto'.ljust(25), ':', num1 != num2)
print(''.center(50, '-'))

# --------------------- LOGICA ---------------------------------------
print('Logical Tables'.center(25))
print(''.center(25, '-'))

print(' AND '.center(25, '#'))
print('False'.ljust(7), 'False'.ljust(7), ':', False and False)
print('False'.ljust(7), 'True'.ljust(7), ':', False and True)
print('True'.ljust(7), 'False'.ljust(7), ':', True and False)
print('True'.ljust(7), 'True'.ljust(7), ':', True and True)

print(' OR '.center(25, '#'))
print('False'.ljust(7), 'False'.ljust(7), ':', False or False)
print('False'.ljust(7), 'True'.ljust(7), ':', False or True)
print('True'.ljust(7), 'False'.ljust(7), ':', True or False)
print('True'.ljust(7), 'True'.ljust(7), ':', True or True)

print(' NOT '.center(25, '#'))
print(''.ljust(7), 'False'.ljust(7), ':', not False)
print(''.ljust(7), 'True'.ljust(7), ':', not True)
print(''.center(25, '-'))

