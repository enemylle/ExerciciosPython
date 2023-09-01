'''Faça um programa que leia um ano qualquer e mostre se ele é Bissesxto'''
print('É ou não é um ano bissexto? ')
from datetime import date
ano = int(input('Informe o Ano que quer analisar? Digite 0 para analisar o ano atual:  '))

if ano == 0:
  ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano {} é bissexto. '.format(ano))
else:
  print('O ano {} não é bissexto. '.format(ano))
  
  
  