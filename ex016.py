'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.'''
import math

num = float(input('Digite um número: '))
print('O número real é {} e sua porção inteira é {}'.format(num, math.trunc(num)))