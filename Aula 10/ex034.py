"""
Aula 10

Exercício 034 - Aumentos múltiplos

Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.

Para salários superiores a R$1.250,00 calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.
"""

print('=' * 10, 'DESAFIO 034', '=' * 10)

# Entrada de dados
salario = float(input('Qual é o salário do funcionário? R$'))

# Verificação do tamanho dos valores
if salario > 1250:
    # Cálculo se for maior do que R$1.250,00
    novo_salario = salario + (salario * 0.10)
else:
    # Cálculo se for menor ou igual do que R$1.250,00
    novo_salario = salario + (salario * 0.15)

# Saída de dados
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo_salario))
