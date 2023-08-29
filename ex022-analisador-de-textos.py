'''Crie um programa que leia o nome
completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas.
O nome com todas as letras minúsculas.
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome.'''

print('Analisador de Textos')

nome = str(input('Digite o nome completo. ')).strip()
print('Analisando seu nome...')

print('Seu nome completo:  ' ,(nome))
print('Seu nome em letras Maiúsculas: \n {} ' .format(nome.upper()))
print('Seu nome em letras minúsculas: \n {} ' .format(nome.lower()))
print('Seu nome completo tem {} letras. ' .format(len(nome)-nome.count(' ')))

div=nome.split()
print('Seu primeiro nome {} tem {} letras. '.format(div[0], len(div[0])))