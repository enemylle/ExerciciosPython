#faça um algoritmo que leia o preço de um produto
# e mostre um novo preço com 5% de desconto.

preço = float(input('Qual o valor do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço , novo))