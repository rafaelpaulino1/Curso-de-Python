"""
Aula 10

Exercício 028 - Jogo da Adivinhação v.1.0

Escreva um prograna que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
# Importação da Função "randint" da Biblioteca "random"
from random import randint

# Importação da função "sleep" da Biblioteca "time"
from time import sleep

print('=' * 10, 'DESAFIO 028', '=' * 10)

# Apresentação do Programa
print('\33[0;33m-=-' * 20, '\33[m')
print('\33[0;34mVou pensar em um número entre 0 e 5. Tente adivinhar...\33[m')
print('\33[0;33m-=-' * 20, '\33[m')

# Leitura do número inserido pelo usuário
num_r = int(input('Em que número eu pensei? '))

print('\33[0;35mPROCESSANDO...\33[m')
sleep(3)

# Gerador do número entre 0 e 5
num_a = randint(0, 5)

# Condição para saber se o usuariuo acertou ou errou o número
if num_r == num_a:
    # Reposta se acertar
    print('\33[0;32mPARABÉNS! Você conseguiu me vencer!\33[m')
else:
    # Resposta se errar
    print('\33[0;31mGANHEI! Eu pensei no número {} e não no {}!'.format(num_a, num_r), '\33[m')
