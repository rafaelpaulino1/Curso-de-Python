"""
Aula 13

Exercício 051 - Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de um PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('=' * 10, 'DESAFIO 051', '=' * 10)

print('=' * 30)
print(' ' * 5 + '10 TERMOS DE UMA PA' + ' ' * 5)
print('=' * 30)

termo_pa = int(input('Primeiro termo: '))  # Variável para receber o primeiro valor da PA
razao = int(input('Razão: '))  # Varaiável para receber o valor da razão

# Laço para fazer o cáclculo da PA e imprimir os valores
for x in range(0, 10):
    print('{} -> '.format(termo_pa), end='')  # Saída dos valores
    termo_pa += razao  # Cálculo da PA

print('ACABOU')
