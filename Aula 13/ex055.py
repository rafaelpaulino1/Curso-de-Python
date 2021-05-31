"""
Aula 13

Exercício 055 - Maior e menor da sequência

Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 055', '=' * 10)
print('*-' * 18)

peso_menor = 0  # Variável para o menor peso
peso_maior = 0  # variável para o maior peso

# Laço para receber o peso e ver qual o maior e menor peso
for c in range(1, 6):
    
    peso = float(input('Peso da {}ª pessoa: '.format(c)))  # Entrada de dados
    
    # Condição para definir maior e menor peso
    if c == 1:  # definir primeiro maio/menor peso
        peso_menor = peso
        peso_maior = peso
    else:
        if peso > peso_maior:  # definir maior peso
            peso_maior = peso
        
        if peso < peso_menor:  # definir menor peso
            peso_menor = peso

# Saída de dados
print('O maior peso lido foi de {:.1f}Kg'.format(peso_maior))
print('O menor peso lido foi de {:.1f}Kg'.format(peso_menor))
