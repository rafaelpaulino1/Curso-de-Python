"""
Aula 13

Exercício 052 - Números primos

Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 052', '=' * 10)
print('*-' * 18)

num = int(input('Digite um número: '))  # Entrada de dados

cont = 0  # Váriavel para verificar a quantidade de números dsivisíveis

# Laço para saber se o número é primo e imprimi-lo 
for c in range(1, num + 1):
    
    #  Condição para saber se o número digitado é primo
    if num % c == 0 and num % num == 0:  
        print('\033[33m', c,'\033[m', end='')  # Saída se o número for divisível (AMARELO)
        cont += 1
    else: 
        print('\033[31m', c,'\033[m', end='')  # Saída se o número não for divisível (VERMELHO)

print('\nO número {} foi divisível {} vezes'.format(num, cont))

# Condição para saída
if cont == 2:
    print('E por isso ele É PRIMO!')  # Saída se for primo
else:
    print('E por isso ele NÃO É PRIMO!')  # Saída se não for primo
