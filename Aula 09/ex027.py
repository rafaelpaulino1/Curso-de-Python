"""
Aula 09

Exercício 027 - Primeiro e ultimo nome de uma pessoa

Faça um programa que leia o nome de uma pessoa, mostrando em seguida o
primeiro e o último nome separadamente.
Ex:
Ana Maria de Souza

primeiro = Ana
último = Souza
"""

print('=' * 10, 'DESAFIO 027', "=" * 10)

# Entrada de dados

nome = str(input('Digite seu nome completo: ')).strip().split()

# Saida dos dados

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[-1]))
