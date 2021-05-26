"""
Aula 13

Exercício 049 - Tabuada v.2.0

Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for.
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 049', '=' * 10)
print('*-' * 18)

num = int(input('Digite um número para ver sua tabuada: '))  # Entrada de dados

# Laço para fazer a tabuada do valor 'num'
for x in range(1, 11):
    print('{} X {:2} = {}'.format(num, x, num * x))  # Saída de dados
