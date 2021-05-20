"""
Aula 09

Exercício 023 - Separando dígitos de um número

Faça um programa que leia um número de 0  a 9999 e mostre na tela cada
um dos dígitos separados.

Ex:
Digite um número:1834

unidade: 4
dezena: 3
centena: 8
milhar: 1
"""
print('=' * 10, 'DESAFIO 023', '=' * 10)

# Entrada de dados

num = str(input('Informe um número: '))

print('Analisando o número {}'.format(num))

# Saída dos dados

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
