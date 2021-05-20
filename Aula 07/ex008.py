"""
Aula 07 - Ecreva um programa que leia um valor em metros
e o exiba convertido em centimetros e milimetros.
"""

print('='*10, 'DESAFIO 08', '='*10)

num = float(input('Digite um valor em metros: '))

cent = num * 100
mili = num * 1000

print('O valor {}m convertido em centimetros é {:.0f}cm e em milimetros é {:.0f}mm'.format(num, cent, mili))
