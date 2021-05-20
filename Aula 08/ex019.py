"""
Aula 08

Exercício 019 - Sorteando um item na lista

Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do
escolhido.
"""

# Importação da Função "choice" da Biblioteca "random"
from random import choice

print('=' * 10, 'DESAFIO 019', '=' * 10)

# Entrada de dados
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

# Saída de dados com o sorteio
print('O aluno escolhido foi o(a) {}.'.format(choice([aluno1, aluno2, aluno3, aluno4])))
