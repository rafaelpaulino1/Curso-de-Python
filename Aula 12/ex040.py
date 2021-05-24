"""
Aula 12

Exercício 040 - Aquele clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERÇÃO
- Média 7.0 ou superior: APROVADO
"""

print('*-'*18)
print('=' * 10, 'DESAFIO 040', '=' * 10)
print('*-'*18)

# Entrada de dados
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

# Cáculo para saber a média do aluno
media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:1.f}, a media do aluno é {:1f}'.format(nota1, nota2, media))

# Condição para saber a situação do aluno
if media < 5.0:
    # Saída se o aluno está aprovado
    print('O Aluno está REPROVADO.')
elif 5.0 <= media <= 6.9:
    # Saída se o aluno esta em recuperação
    print('O aluno está em RECUPERAÇÃO')
elif media >= 7.0:
    # Saída se o aluno reprovou
    print('O aluno está APROVADO')
