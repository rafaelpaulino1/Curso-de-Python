"""
Aula 08

Exercício 018 - Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
"""

# Importação das Funções "sin", "cos" e "tan" da Biblioteca "math"
from math import sin, cos, tan, radians

print('=' * 10, 'DESAFIO 018', '=' * 10)

# Entrada de dados
num_x = int(input('Digite o valor de um ângulo: '))

# Saída de dados já com os cálculos feitos
print('O Seno do número {} é {:.2f}.'.format(num_x, sin(radians(num_x))))
print('O Cosseno do número {} é {:.2f}.'.format(num_x, cos(radians(num_x))))
print('A Tangente do número {} é {:.2f}.'.format(num_x, tan(radians(num_x))))
