"""
Aula 07 - Faça um programa que leia quanto dinheiro
uma pessoa tem na carteira e mostre quantos Dólares
ela pode comprar.

Considere
US$1,00 = R$3,27  (Saudades ;-;).
"""

print('='*10, 'DESAFIO 10', '='*10)

din = float(input('Digite a quantidade de dinheiro que você possui na carteira:'))

conv = din / 3.27

print('\nSeu dinheiro convertido em dólar seria: US${:.2f}'.format(conv))
