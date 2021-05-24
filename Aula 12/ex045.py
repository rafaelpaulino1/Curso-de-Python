"""
Aula 12

Exercício 045 - GAME: Pedra, Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.
"""

print('*-' * 18)
print('=' * 10, 'DESAFIO 045', '=' * 10)
print('*-' * 18)

from time import sleep
from random import randint

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

usuario = int(input('Qual é a sua jogada? '))  # Escolha do USUARIO
sleep(0.5)

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

computador = randint(0, 2)  # Escolha do COMPUTADOR

print('-=' * 13)
# Saída da escolha da máquina
if computador == 0:
    print('Computador jogou PEDRA')
elif computador == 1:
    print('Computador jogou PAPEL')
elif computador == 2:
    print('Computador jogou TESOURA')

# Saída da escolha do jogador
if usuario == 0:
    print('Jogador jogou PEDRA')
elif usuario == 1:
    print('Jogador jogou PAPEL')
elif usuario == 2:
    print('Jogador jogou TESOURA')
else:
    print('OPÇÃO INVÁLIDA! Tente Novamente.')

print('-=' * 13)

# Condições de vitória, derrota ou empate

# EMPATE
if usuario == computador:
    print('EMPATE')

# VITORIAS USUARIO
elif usuario == 0 and computador == 2:
    print('JOGADOR VENCE')
elif usuario == 1 and computador == 0:
    print('JOGADOR VENCE')
elif usuario == 2 and computador == 1:
    print('JOGADOR VENCE')

# VITORIAS COMPUTADOR
elif computador == 0 and usuario == 2:
    print('COMPUTADOR VENCE')
elif computador == 1 and usuario == 0:
    print('COMPUTADOR VENCE')
elif computador == 2 and usuario == 1:
    print('COMPUTADOR VENCE')
