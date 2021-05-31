"""
Aula 13

Exercício 056 - Analisador completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""
print('*-' * 18)
print('=' * 10, 'DESAFIO 056', '=' * 10)
print('*-' * 18)

# Variáveis usadas no laço
soma_idade = 0
maior_idade = 0 
guarda_nome = ''
cont_idade = 0


 # Laço para receber os dados do usuario; 
 # fazer a soma de idades;  
 # guardar o nome do homem mais velho; 
 # contar quantidade de mulhers com menos de 20 anos.
for c in range(1, 5):
    print('-' * 5, '{}ª PESSOA'.format(c), '-' * 5)
    
    nome = str(input('Nome: '))  # Variável que recebe o nome do usuário
    idade = int(input('Idade: '))  # Variável que recebe a idade do usuário
    sexo = str(input('Sexo [M/F]: '))  # Variável que recebe o sexo do usuário

    soma_idade += idade  # Soma de idades 

    # Condição para guardar maior idade e nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        guarda_nome = nome

    # Condição para fazer a contagem de idades femininas
    if sexo == 'F' and idade < 20:
        cont_idade += 1

media_idade = soma_idade / 4  # média de idades


# Saída de dados
print('A média de idade do grupo é de {:.1f} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade, guarda_nome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont_idade))
