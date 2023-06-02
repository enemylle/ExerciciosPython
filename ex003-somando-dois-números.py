# crie um programa que leia dois números e mostre a soma entre eles.
# int antes do input declara o valor primitivo, no caso int é um numérico.
a = int(input('digite um número '))
b = int(input('Digite outro número. '))
s = a + b
#print ('o resultado de',a, '+',b, 'é igual à', s)
print ('A soma de {} e {} vale {}' .format(a,b,s))
