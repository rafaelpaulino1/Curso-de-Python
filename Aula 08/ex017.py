"""
Aula 08

Exercício 017 - Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
# Importação da Função "hipot" da Biblioteca "math"
from math import hypot

print('=' * 10, 'DESAFIO 017', '=' * 10)

# Entrada de dados
cat_a = float(input('Digite o valor do cateto "A": '))
cat_b = float(input('Digite o valor do cateto "B": '))

# Saída de dados já com o resultado da hipotenusa
print('A hipotenusa é igual a {:.2f}'.format(hypot(cat_a, cat_b)))
