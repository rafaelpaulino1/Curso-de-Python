"""
Aula 13

Exercício 050 - Soma dos pares

Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 050', '=' * 10)
print('*-' * 18)

cont = 0  # Variável para fazer a contagem dos valores pares
soma = 0  # Variável para fazer a soma dos valores pares

# Laço para pedir o valor fazer a contagem e a soma dos valores
for x in range(1, 7):
    num = int(input('Digite o {}º número: '.format(x)))
    if num % 2 == 0:
        cont += 1  # Soma para contagem dos valores
        soma += num  # Soma total dos valores

print('Você informou {} número(s) PARES e a soma foi {}'.format(cont, soma))  # Saída dos valores
