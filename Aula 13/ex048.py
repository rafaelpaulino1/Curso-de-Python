"""
Aula 13

Exercício 048 - Soma ímpares múltiplos de três

Faça um progama que calcule a soma entre todos os números ímpares que são múltiplos
de três e que se encontram no intervalo de 1 até 500.
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 048', '=' * 10)
print('*-' * 18)

soma = 0  # Variável para fazer o somatório dos valores
cont = 0  # Variável para fazer a contagem de valores

# Laço para fazer a contagem e somatório dos valores
for x in range(0, 501, 3):
    # Condição para saber se é ímpar
    if x % 2 == 1:
        cont += 1  # Soma para contagem dos valores
        soma += x  # Soma total dos valores

print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))  # Saída dos dados
