# crie um programa que leia dois números e mostre a soma entre eles.
# int antes do input declara o valor primitivo, no caso int é um numérico.
a = int(input('digite um número '))
b = int(input('Digite outro número. '))
s = a + b
cores = {'azul':'\033[34m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'limpa':'\033[m',}
#print ('o resultado de',a, '+',b, 'é igual à', s)
print ('A soma de {}{}{} e {}{}{} vale {}{}{}' .format(cores['azul'], a, cores['limpa'],cores['vermelho'], b, cores['limpa'], cores['verde'], s, cores['limpa']))
