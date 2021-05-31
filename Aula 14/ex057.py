"""
Aula 14

Exercício 057 - Validação de dados

Faça um Programa que leia o sexo de uma pessoa, mas só aceite os valores 'M'
ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
print('=-' * 17)
print('=' * 10, 'DESAFIO 056', '=' * 10)
print('=-' * 17)

sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]  # Variável para receber o sexo do usuário

x = 0  # Variável para iniciar o laço de repetição

# Laço para verificar se os dados estão corretos
while x != 1:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]  # Receber o valor correto
    
    # Condição caso o usuario digite o valor correto
    if sexo == 'M'  or sexo == 'F':
        x = 1  # Encerra o laço

print('Sexo {} registado com sucesso.'.format(sexo))  # Saída de dados
