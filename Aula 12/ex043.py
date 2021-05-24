"""
Aula 12

Exercício 043 - índice de Massa Corporal

Desenvolva uma lógica que leia o peso e a altura de uma pessoa,calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 043', '=' * 10)
print('*-' * 18)

# Entrada de dados
peso = float(input('Qual é o seu peso? (Kg) '))  # Entrada de peso
altura = float(input('Qual é a sua altura? (m) '))  # Entrada de altura

imc = peso / (altura ** 2)  # Cálculo para saber o imc

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

# Condição para saber o status do usuario
if imc < 18.5:
    # ABAIXO DO PESO
    print('Você está abaixo ABAIXO DO PESO ideal')
elif 18 <= imc < 25:
    # PESO IDEAL
    print('PARÁBENS, você está na faixa de PESO IDEAL')
elif 25 <= imc < 30:
    # SOBREPESO
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    # OBESIDADE
    print('Você está em OBESIDADE!')
else:
    # OBESIDADE MÓRBIDA
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
