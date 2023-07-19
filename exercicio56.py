'''
Exercício Python 056: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
soma_idade = 0
maior_idade = 0
nome_velho = None
f = 0

for i in range(1,5):
    print(f'{i}ª Pessoa')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo - [M]/[F]').strip().lower()

    soma_idade += idade

    if sexo == 'f' and idade < 20:
        f += 1

    if sexo == 'm':
        maior_idade = idade
        nome_velho = nome
    
        if maior_idade < idade:
            maior_idade = idade
            nome_velho = nome
         
media_idades = int(soma_idade/ i)    

print(f'A média das idades do grupo é de {media_idades} anos')
print()
print(f'{f} mulheres tem menos de 20 anos.')
print()
print(f'O homem mais velho é o {nome_velho}')