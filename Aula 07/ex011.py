"""
Aula 07 - Faça um programa que leia a largura e a altura
de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pinta-la, sabendo que cada litro
de tinta, pinta uma área de 2m².
"""

print('='*10, 'DESAFIO 11', '='*10)

# Entrada de dados
lar = float(input('Digite a largura da parede em metros:'))
alt = float(input('Digite a altura da parede em metros:'))

# Cálculo para medir a area da parede
area = lar * alt

# Cálculo para medir a quantidade necessária
qntd_tinta = area / 2


#Saída de dados
print('A área da parede é: {:.2f}m²'.format(area))

print('A quantidade de tinta necessária para pintar a parede é: {:.4f}l'.format(qntd_tinta))