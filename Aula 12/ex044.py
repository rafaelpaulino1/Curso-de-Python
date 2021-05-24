"""
Aula 12

Exercício 044 - Gerenciador de Pagamentos

Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x vezes ou mais no cartão: 20% de juros
"""

print('=' * 10, 'DESAFIO 044', '=' * 10)

print('{:=^40}'.format(' LOJAS PAULINO '))

# Entrada de dados
valor_compra = float(input('Preço das compras:  R$'))

print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")

# Definir opção de pagamento
resposta = int(input('Qual é a opção? '))

# Condição para excutar a opção de pagamento desejada
if resposta == 1:
    # A vista
    desconto = valor_compra - (valor_compra * 10 / 100)  # Cálculo desconto 10%

    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor_compra, desconto))  # Saída de dados
elif resposta == 2:
    # A vista no cartão
    desconto = valor_compra - (valor_compra * 5 / 100)  # Cáculo desconto 5%

    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor_compra, desconto))  # Saída de dados
elif resposta == 3:
    # 2x no cartão
    parcelas = valor_compra / 2  # Cálculo de parcelas (2x)

    print('Sua compra de R${:.2f} vai ficar em 2x parcelas de R${:.2f} SEM JUROS'.format(valor_compra, parcelas))  # Saúida de dados
elif resposta == 4:
    # 'n'x no cartão
    qtd_parc = int(input('Quantas parcelas? '))  # Definir quantidade de parcelas

    juros = (valor_compra + (valor_compra * 20 / 100))  # Cálculo juros 20%

    parcelas = juros / qtd_parc  # Cáculo de parcelas

    #Saída de dados
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(qtd_parc, parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor_compra, juros))
else:
    # Saída de opção inválida
    print('Opção inválida! Tente novamente.')
