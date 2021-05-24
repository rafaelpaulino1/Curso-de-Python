"""
Aula 12

Exercício 042 - Analisando Triângulos v2.0

Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

print('=' * 10, 'DESAFIO 042', '=' * 10)

print('-=' * 20)
print('Analisador de Triângulos', ' '*13, '|')
print('-=' * 20)

# Entrada de dados
lado_a = float(input('Primeiro segmento: '))
lado_b = float(input('Segundo segmento: '))
lado_c = float(input('Terceiro segmento: '))

# Condição para saber se forma um triângulo e qual tipo
if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_c + lado_a > lado_b:
    if lado_a == lado_b == lado_c:
        # Resposta se forma triângulo EQUILATERO
        print('Os segmentos acima PODEM FORMAR triângulo EQUILÁTERO!')
    elif lado_a != lado_b != lado_c != lado_a:
        # Resposta se formar triângulo ESCALENO
        print('Os segmentos acima PODEM FORMAR triângulo ESCALENO')
    else:
        # Resposta se formar triângulo ISOSCELES
        print('Os segmentos PODEM FORMAR triângulo ISÓSCELES')
else:
    # Resposta se não forma triângulo
    print('Os segmentos NÃO PODEM FORMAR triângulo!')
