"""
Aula 10

Exercício 033 - Maior e menor valores

Faça um programa que leia três números e mostre qual é o maior e
qual é o menor.
"""

print('=' * 10, 'DESAFIO 033', '=' * 10)

# Entrada de dados
num_1 = float(input('Primeiro valor: '))
num_2 = float(input('Segundo valor: '))
num_3 = float(input('Terceiro valor: '))

# Verificação do menor valor
if num_1 < num_2 and num_1 < num_3:
    menor = num_1
if num_2 < num_1 and num_2 < num_3:
    menor = num_2
if num_3 < num_1 and num_3 < num_2:
    menor = num_3

# Verificação do maior valor
if num_1 > num_2 and num_1 > num_3:
    maior = num_1
if num_2 > num_1 and num_2 > num_3:
    maior = num_2
if num_3 > num_1 and num_3 > num_2:
    maior = num_3

# Saída de dados
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
