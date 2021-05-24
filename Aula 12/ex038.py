"""
Aula 12

Exercício 038 - Comparando números

Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

print('=' * 10, 'DESAFIO 038', '=' * 10)

# Entrada de dados
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

# Condição para motrar qual é o maior valor ou se são iguais
if num1 > num2:
    # Saída se o primeiro valor for maior
    print('O PRIMEIRO valor é maior')
elif num2 > num1:
    # Saída se o segundo valor for maior
    print('O SEGUNDO valor é maior')
else:
    # Saída se os valores forem iguais
    print('Os dois valores são IGUAIS')
