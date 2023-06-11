##faça um algoritmo que leia o salário de um funcionário
## e mostre o seu novo salário com 15% de aumento.

salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('O funcionário que recebia R${:.2f} agora com o acrécimo de 15% receberá R${:.2f}'.format(salário, novo))
