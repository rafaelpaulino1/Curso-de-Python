"""
Aula 07 - Faça um algoritmo que leia o preço de um
produto e mostre seu novo preço, com 5% de desconto.
"""

print('=' * 10, 'DESAFIO 12', '=' * 10)

# Entrada de dados
valor = float(input('Digite o valor do produto para saber o desconto:'))

# Cálculo de desconto de 5%
desc = valor - (valor * 0.05)

# Saída de dados
print('\nO valor de R${:.2f} com 5% de desconto é: R${:.2f}'.format(valor, desc))
