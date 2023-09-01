'''Faça um programa que leia três números
e mostre qual é o maior e qual é o menor'''

a = int(input('Digite o primeiro número. '))
b = int(input('Digite o segundo. '))
c = int(input('Digite o terceiro. '))
'''if a<b and a<c:
  menor = a
if b<c and b<a:
  menor = b
if c<a and c<b:
  menor = c'''
menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c
print('Menor: {}' .format(menor))

maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
print('Maior: {}' .format(maior))

  
