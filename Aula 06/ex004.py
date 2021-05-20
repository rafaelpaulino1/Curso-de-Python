"""
Aula 06 - Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas
as informações possíveis sobre ele.
"""

print('========DESAFIO 04========')

var = input('Digite algo:')

print('Tipo de Variável: {}'.format(type(var)))
print('É alfanúmerico? {}'.format(var.isalnum()))
print('É númerico? {}'.format(var.isnumeric()))
print('É alfabético? {}'.format(var.isalpha()))
print('É ASCII? {}'.format(var.isascii()))
print('É um digito? {}'.format(var.isdigit()))
print('Só tem espaços? {}'.format(var.isspace()))
