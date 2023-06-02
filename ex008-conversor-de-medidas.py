# escreva um progeama que leia o valor em metros e o exiba convertido em centimetros e milimetros.
## km hm dam m dm cm mm ##
medida = float(input('Digite uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('{}km \n {}hm \n {}dam \n {}dm \n {}cm \n{}mm \n '.format(
    km, hm, dam, dm, cm, mm))
