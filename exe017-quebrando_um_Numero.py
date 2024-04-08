
Exercício Python 17: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Ex:
# Digite um número: 6.127
# O número 6,127 tem a parte inteira 6.

#Usei a classe math


from math import trunc
num = float(input('Digite um número: '))
print('O número digitado foi {}, e sua parte inteira é {} '.format(num, trunc(num)))        #,trunc: é trunquete, ele corta a parte inteira do número


'''Codigo usando a importação da biblioteca inteira:

import math
num = float(input('Digite um número: '))
print('O número digitado foi {}, e sua parte inteira é {} '.format(num, math.trunc(num)))'''
