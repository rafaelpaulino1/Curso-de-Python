"""
Aula 13

Exercício 047 - Contagem de pares

Crie um programa que mostre na tela todos os números pares que estão no intervalo
entre 1 e 50.
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 047', '=' * 10)
print('*-' * 18)

# Repetição para mostrar números pares
for cont in range(2, 51, 2):
    print(cont, end=' ')  # Mostrar valor atual do contador pulando de 2 em 2
print('ACABOU')
