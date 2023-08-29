'''Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com a palavra "SANTO" '''

cidade=str(input('Digite um nome de Cidade: ').upper().strip())
print(cidade[:5] == 'SANTO')