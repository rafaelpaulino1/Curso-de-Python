"""
Aula 10

Exercício 030 - Par ou Ímpar

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR
ou ÍMPAR.
"""

print('='*10, 'DESAFIO 030', "="*10)

# Leitura do valor inteiro
num = int(input('\33[35mMe diga um número qualquer:\33[m '))

# Cálculo para verificar se impar ou par
verificar = num % 2

# Condição de resposta
if verificar == 0:

    # Reposta se for Par
    print('O número {} é \33[34mPAR\33[m'.format(num))

else:

    # Resposta se for Impar
    print('O número {} é \33[34mIMPAR\33[m'.format(num))
