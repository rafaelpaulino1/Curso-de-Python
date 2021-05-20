"""
Aula 08

Exercício 016 - Quebrando um número

Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""

# Importação da Função "trunc" da Biblioteca "math"
from math import trunc

print('=' * 10, 'DESAFIO 016', '=' * 10)

# Leitura de Dados
num = float(input('Digite um número: '))

# Sáida de Dados com o valor já truncado
print('O número {} tem a parte inteira {}'.format(num, trunc(num)))
