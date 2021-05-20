"""
Aula 09

Exercício 026 - Primeira e ultima ocorrência de uma string

Faça um programa que leia uma frase pelo teclado e mostre:

@ Quantas vezes aparece a letra "A"
@ Em que posição ela aparece a primeira vez
@ Em que posição ela aparece a última vez.
"""

print('=' * 10, 'DESAFIO 026', '=' * 10)

# Entrada de dados

frase = str(input('Digite uma frase: ')).strip().upper()

# Saída de dados com de letras A

print('A letra A aparace {} vezes na frase'.format(frase.count('A')+1))

# Posições da letra A

print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
