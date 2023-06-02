real = float(input('Quanto de dinheiro vc tem na carteira? R$'))
dolar = real / 5.01
euro = real / 5.40

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real,dolar))
print('Com R${:.2f} você pode comprar EUR €{:.2f}'.format(real,euro))