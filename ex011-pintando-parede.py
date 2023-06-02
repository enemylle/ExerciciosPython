## Faça um programa que leia a altura e a largura de uma parede em metros. 
# calcule a sua área e a quantidade de tinta para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input(' Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))
area = larg * alt
print('Sua parede tem a dimensão de {}X{} e a sua área é de {:.2f}m² '.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede vc precisará de {}L de tinta'.format(tinta))