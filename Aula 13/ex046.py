"""
Aula 13

Exercício 046 - Contagem Regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
print('*-' * 17)
print('=' * 10, 'DESAFIO 046', '=' * 10)
print('*-' * 17)

from time import sleep  # Importação da Função 'sleep' da Biblioteca 'time'

# Contador com índice invertido
for cont in range(10, -1, -1):
    print(cont)  # Mostrar valor atual da contagem
    sleep(1)  # Pausar o programa por 1 segundo
print('BUM! BUM! POOW!')
