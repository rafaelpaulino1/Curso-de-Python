"""
Aula 10

Exercício 032 - Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSESXTO.
"""

print('=' * 10, 'DESAFIO 032', '=' * 10)

# Iportação da Função 'date' da Biblioteca 'datetime'
from datetime import date

# Leitura do ano
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

# Pegar o ano atual da máquina
if ano == 0:
    ano = date.today().year

# Condição para saber se o ano é Bissexto
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    # Resposta se o ano é Bissexto
    print('O ano de {} é BISSEXTO!'.format(ano))
else:

    # Resposta se o ano não é Bissexto
    print('O ano de {} NÃO É BISSEXTO!'.format(ano))
