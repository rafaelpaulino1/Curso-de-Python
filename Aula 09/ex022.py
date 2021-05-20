"""
Aula 09

Exercício 022 - Analisador de Textos

Crie um programa que leia o nome completo de
uma pessoa e mostre:

@ O nome com todas as letras maísculas
@ O nome com todas minúsculas
@ Quantas letras ao no total (sem considerar espaços)
@ Quantas letras tem o primeiro nome
"""

print('=' * 10, 'DESAFIO 022', '=' * 10)

# Entrada de dados

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')

# Saída de dados com nome maiúsculo e minúsculo

print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))

# Sáida do nome com quantidade de letras

print('Seu nome tem ao todo {} letras'.format(len(nome.replace(' ', ''))))

# Separação do nome em um lista
nome_dividido = nome.split()

# Saida do primeiro nome e a quantidade de letras

print('Seu primeiro nome é {} e ele tem {} letras'.format(nome_dividido[0], len(nome_dividido[0])))
