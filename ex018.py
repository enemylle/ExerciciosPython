'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo'''
import math 
ângulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(ângulo))
cos = math.cos(math.radians(ângulo))
tan = math.tan(math.radians(ângulo))
print('O valor de seno é {:.2f} cosseno {:.2f} tangente {:.2f}.' .format(seno, cos, tan))