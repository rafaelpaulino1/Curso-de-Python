"""
Aula 07 - Faça um algoritmo que leia o salário de um
funcionário e mostre seu novo salário, com 15% de aumento.
"""

print('=' * 10, 'DESAFIO 13', '=' * 10)

# Entrada de dados
sal = float(input('Digite seu salário: R$'))

# Cálculo com 15% de aumento
aum = sal + (sal * 0.15)

# Saída de dados
print('\nSeu salário de R${:.2f} aumentou para: R${:.2f}'.format(sal, aum))
