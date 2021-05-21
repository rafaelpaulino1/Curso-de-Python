"""
Aula 12

Exercício 036 - Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele
vai pagar.

Calcule o valor da pretação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""
print('=' * 10, 'DESAFIO 036', '=' * 10)

# Entrada de dados
valor_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano_fin = int(input('Quantos anos de financiamento? '))

# Cáculo para saber o valor das prestações
prestacoes = valor_casa / (ano_fin * 12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor_casa, ano_fin, prestacoes))

# Condição para saber se o empréstimp será negado ou não
if prestacoes <= (salario * 30 / 100):
    # Resposta se for concedido
    print('Empréstimo pode ser CONCEDIDO!')
else:

    # Resposta se for negado
    print('Empréstimo NEGADO!')
