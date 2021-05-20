"""
Aula 10

Exercício 029 - Radar eletrônico

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km\h, mostre uma mensagem dizendo que ele
foi multado.

A multa vai custar R$7,00 por cada Km acima do limite.
"""

print('='*10, 'DESAFIO 029', "="*10)

# Leitura dos dados (km)

velocidade_carro = float(input('Qual é a velocidade do carro? '))

# Verificar se a velocidade é maior que 80km
if velocidade_carro > 80.0:

    # Cálculo de multa
    multa = (velocidade_carro-80.0) * 7.0

    # Saída de dados
    print('\33[0;31mMULTADO! Você excedeu o limite permitido que é de 80km/h\n'
          'Você deve pagar um multa de\33[m \33[0;33mR${:.2f}!\33[m'.format(multa))

print('\33[0;32mTenha um bom dia! Dirija com segurança!\33[m')
