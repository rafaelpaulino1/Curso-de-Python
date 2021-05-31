"""
Aula 13

Exercício 053 - Detector de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é palíndromo,
desconsiderando os espaços.

Ex: APOS A SOPA
"""

print('*-' * 18)
print('=' * 10, 'DESAFIO 053', '=' * 10)
print('*-' * 18)

texto = str(input('Digite uma frase: ')).replace(' ','').upper()  # Entrada do texto

texto_invertido = texto[::-1].replace(' ','').upper()  # Inverte o texto

print('O inverso de {} é {}'.format(texto, texto_invertido))

# Condição para saber se é um palíndromo
if texto == texto_invertido:
    print('Temos um palíndromo!')  # Saída se for um palíndromo
else:
    print('A frase digitada não é um palíndromo')  # Saída se não for um palíndromo
