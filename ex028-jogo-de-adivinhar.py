'''Exercício Python 028: Escreva um programa 
que faça o computador 
"pensar" em um número inteiro entre 0 e 5 e peça para 
o usuário 
tentar descobrir qual foi o número escolhido 
pelo computador. 
O programa deverá escrever na tela se 
o usuário venceu ou perdeu.'''

print('Jogo de Adivinhação')

import random
num = random.randint(0,5)
res = int(input('Tente adivinhar qual número de 0 a 5 o computador escolheu. '))
if res == num:
  print('Parabéns! Você acertou!!!')
else:
  print('Você Perdeu!!!')
