"""
Aula 12

Exercício 041 - Classificando Atletas

A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""

print('*-'*18)
print('=' * 10, 'DESAFIO 041', '=' * 10)
print('*-'*18)

# Importação da Função 'date' da Biblioteca 'datetime'
from datetime import date

# Entrada de dados
ano_nasc = int(input('Ano de nascimento: '))

# Função para pegar o ano atual
ano_atual = date.today().year

# Cáclculo para saber a idade do usuário
idade = ano_atual - ano_nasc

print('O atleta tem {} anos.'.format(idade))

# Condição para saber a classificação do usuario
if idade <= 9:
    # Saida se for MIRIM
    print('CLASSSIFICAÇÃO: MIRIM')
elif idade <= 14:
    # Saida se for INFANTIL
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    # Saida se for JUNIOR
    print('CLASSIFICAÇÃO: JUNIOR')
elif idade <= 25:
    # Saida se for SENIOR
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    # Saida se for MASTER
    print('CLASSIFICAÇÃO: MASTER')
