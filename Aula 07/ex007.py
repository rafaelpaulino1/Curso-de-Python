"""
Aula 07 - Desenvolva um programa que leia as
duas notas de um aluno, calcule e mostre a sua média.
"""

print('='*10, 'DESAFIO 07', '='*10)

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1+nota2)/2

print('A média das duas notas é {:.1f}'.format(media))
