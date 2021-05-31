"""
Aula 13

Exercício 054 - Grupo da Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 054', '=' * 10)
print('*-' * 18)

from datetime import date  # Importação da Função 'date' da Biblioteca 'datetime'

ano_atual = date.today().year  # Variável que recebe o ano atual da máquina

cont_maior = 0  # Variável para contar os maiores de idade
cont_menor = 0  # Variável para contar os menores de idade

# Laço para perguntar a idade e contar maiores e moenores de idade
for c in range(1, 8):

    ano_nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))  # Entrada de dados

    idade = ano_atual - ano_nasc  # Idade atual 

    # Condição para saber se é menor ou maior de idade e fazer a contagem
    if idade < 21:
        cont_menor += 1
    else:
        cont_maior += 1

# Saída de dados
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont_maior))
print('E também tivemos {} pessoas menores de idade'.format(cont_menor))
