"""
Aula 10

Exercício 035 - Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas e diga ao
usuário se elas podem ou não formar um triângulo.
"""

print('=' * 10, 'DESAFIO 035', '=' * 10)

print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

# Leitura de dados
lado_a = float(input('Primeiro segmento: '))
lado_b = float(input('Segundo segmento: '))
lado_c = float(input('Terceiro segmento: '))

# Condição para saber se forma um triângulo
if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_c + lado_a > lado_b:

    # Resposta se forma triângulo
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:

    # Resposta se não forma triângulo
    print('Os segmentos NÃO PODEM FORMAR triângulo!')
