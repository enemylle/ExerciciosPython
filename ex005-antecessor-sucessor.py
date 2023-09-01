print('Faça um programa que leia um número inteiro e mostre na tela o valor do seu sucessor e de seu antecessor.')

n = int(input('Digite um Valor: ' ))
cores = {'azul':'\033[34m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'limpa':'\033[m',}

print ('Analizando o valor de {}{}{}, seu sucessor é {}{}{}, e seu antecessor é {}{}{} .'.format(cores['azul'], n, cores['limpa'] , cores['amarelo'], (n+1) ,cores['limpa'], cores['verde'], (n-1), cores['limpa'] ))

