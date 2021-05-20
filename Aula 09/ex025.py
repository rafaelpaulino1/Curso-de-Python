"""
Aula 09

Exercício 025 - Procurando uma string dentro de outra

Crie um programa que leia o nome de uma pessoa e diga se ela
tem "SILVA" no nome.
"""

print('=' * 10, 'DESAFIO 025', '=' * 10)

# Entrada e leitura do nome

nome = str(input('Qual é seu nome completo? ')).strip()

# Saida e verifcação do nome

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
