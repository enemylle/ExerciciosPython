'''Exercício Python 030: 
Crie um programa que leia um número inteiro 
e mostre na tela se ele é PAR ou ÍMPAR.'''
print('O número é Par ou Impar? ')
num = int(input('Digite um número inteiro: '))
print('O número é {} ' .format(num))
if num % 2 == 0:
  print('Par!')
else:
  print('Impar!')