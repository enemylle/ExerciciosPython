'''Exercício Python 031: 
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
de até 200Km e R$0,45 parta viagens mais longas.'''

print('Custo da Viagem')
km = int(input('Digite a distância da viagem. '))
print(km)
km1 = km * 0.50
km2 = km * 0.45
if km <= 200:
  print('A passagem custa R${:.2f}' .format(km1))
else:
  print('A passagem custará R${:.2f}'.format(km2))
  
