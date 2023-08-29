'''Faça um programa que leia o nome de uma pessoa completo,
mostrando em seguida o primeiro e o ultimo nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
último = Souza'''

nome = str(input('Digite o nome de uma pessoa completo. ')).strip()
print('Analizando nome... ')
n=nome.split()
print('Seu primeiro nome é {}.'.format(n[0]))
print('Seu ultimo nome é {}.' .format(n[len(n)-1]))
