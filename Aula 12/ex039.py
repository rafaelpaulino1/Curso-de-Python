"""
Aula 12

Exercício 039 - Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordocom sua idade:

- Se ele ainda vai se alistar ao seviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
print('*-'*18)
print('=' * 10, 'DESAFIO 039', '=' * 10)
print('*-'*18)

# Importação da Função 'date' da Biblioteca 'datetime'
from datetime import date

# Entrada de dados
ano_nasc = int(input('Ano de nascimento: '))

# Função para pegar o ano atual
ano_atual = date.today().year

# Cálculo para saber a idade ataual do usuario
idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} ano(s) em {}'.format(ano_nasc, idade, ano_atual))

# Condição para saber a situção do alistamento militar do usuario
if idade < 18:
    # Saída se o usuario ainda vai se alistar
    print('Ainda faltam {} ano(s) para o alistamento.'.format(18-idade))
    print('Seu alistamento será em {}'.format(ano_atual+(18-idade)))
elif idade > 18:
    # Saida se o usuario ja deveria ter se alistado
    print('Você já deveria ter se alistado há {} ano(s)'.format(idade-18))
    print('Seu alistamento foi em {}'.format(ano_atual-(idade-18)))
elif idade == 18:
    # Saida se o usuario deve se alistar agora
    print('Você tem que se alistar IMEDIATAMENTE!')
