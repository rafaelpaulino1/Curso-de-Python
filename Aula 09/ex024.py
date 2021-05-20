"""
Aula 09

Exercício 024 - Verificando as primeiras letras de um texto

Crie um programa que leia o nome de uma cidade e diga se ela
começa ou não com o nome 'SANTO'.
"""

print('=' * 10, 'DESAFIO 024' '=' * 10)

# Entrada de dados

cidade = str(input('Em que cidade voê nasceu? ')).strip()

# Saída de dados

print(cidade[:5].upper() == 'SANTO')
