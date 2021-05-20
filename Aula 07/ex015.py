"""
Aula 07 - Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15
po Km rodado.
"""

print('=' * 10, 'DESAFIO 15', '=' * 10)

# Entrada de Dados
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

# Cálculos
preco_total = (dias * 60) + (km * 0.15)

# Saída de Dados
print('O total a pagar é de R${:.2f}'.format(preco_total))
