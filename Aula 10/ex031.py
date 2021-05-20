"""
Aula 10

Exercício 031 - Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passgem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.
"""
print('=' * 10, 'DESAFIO 031', '=' * 10)

# Leitura do valor real
dist = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {}Km.'.format(dist))

# Condição para verificar a distância
if dist <= 200:

    # Valor da passagem de R$0.50 por km
    preco = dist * 0.5

else:
    # Valor da passagem de R$0.45 por km
    preco = dist * 0.45

# Saída de dados
print('E o preço da sua passagem será de R${:.2f}'.format(preco))
