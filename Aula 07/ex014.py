"""
Aula 07 - Escreva um programa que converta uma temperatura
digitada em ºC e converta para ºF.
"""

print('=' * 10, 'DESAFIO 14', '=' * 10)

# Entrada de Dados
cels = float(input('Informe a temperatura em ºC: '))

# Cálculo de Conversão de Celsius para Fahrenheit

fahn = ((cels * 9)/5) + 32

# Saída de dados

print('A temperatura de {}ºC corresponde a {}ºF!'.format(cels, fahn))
