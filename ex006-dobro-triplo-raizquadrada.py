## crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('digite um numero: '))

print('\033[1;32manalizando o número \033[m{}\n\033[1;32mseu dobro é \033[m{} \n\033[1;32mseu triplo é \033[m{}\n\033[1;32me a raiz quadrada é \033[m{:.2f} '.format(n, (n*2),(n*3), (n**(1/2))))