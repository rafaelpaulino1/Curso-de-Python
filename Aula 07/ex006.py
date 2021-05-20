"""
Aula 07 - Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e raiz quadrada.
"""

print('='*10, 'DESAFIO 06', '='*10)

num = int(input('Digite um número: '))
"""
Parte Antiga

dobro = num * 2
triplo = num * 3
raizq = num ** (1/2)

print('O dobro do número {} é {}, seu triplo é {} e a sua raiz quadrada é {:.2f}'.format(num, dobro, triplo, raizq))
"""

print('\n O dobro do número {} é {}.\n'.format(num, num*2),
      'O triplo do número {} é {}.\n'.format(num, num*3),
      'A raiz quadrada do número {} é {:.2f}.'.format(num, pow(num, (1/2))))
