"""
Aula 07 - Faça um programa que leia um número inteiro
e mostre na tela o seu sucessor e seu antecessor.
"""

print('='*10, 'DESAFIO 05', '='*10)

num = int(input('Digite um número: '))

print('O número sucessor de {} é {} e o seu antecessor é {}'.format(num, num+1, num-1))
