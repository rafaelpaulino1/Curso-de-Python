"""
Aula 12

Exercício 037 - Conversor de Bases Numéricas

Escreva um programa que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
print('=' * 10, 'DESAFIO 037', '=' * 10)

# Entrada de dados
num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'
      '[ 2 ] converter para OCTAL\n'
      '[ 3 ] converter para HEXADECIMAL')

# Escolha de base de conversão
escolha = int(input('Sua opção: '))

# Condição para saber a escolha e fazer a conversão
if escolha == 1:
    # Fórmula e saída se for binário
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    # Fórmula e sáida se for octal
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    # Fórmula e sáida se for hexadecimal
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    # Saída se for não for definido um tipo válido
    print('TIPO NÃO ENCONTRADO! Tente novamente.')
