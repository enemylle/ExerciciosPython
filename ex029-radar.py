'''Exercício Python 029: Escreva um programa que leia a velocidade 
de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.'''

print('Radar Eletrônico')
km = float(input('Qual a velocidade que o carro atingiu? '))
print('Velocidade {:.2f}km' .format(km))
if km <= 80:
  print('Você não tem multa a pagar!')
else:
  multa = (km-80) * 7
  print('A multa é de R${:.2f} '.format(multa))
