'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

pessoas = []
dados = {}
soma_idades = 0

while True:
    dados.clear()
    dados['nome'] = input('Nome: ')

    while True:
        dados['sexo'] = input('Sexo - [M/F]').upper()[0]

        if dados['sexo'] in 'MF':
            break
        print('Erro. Digite apenas M ou F.')

    while True:
        idade = input('Idade: ')
        idade_int = None

        try:
            idade_int = int(idade)
            dados['idade'] = idade_int
            break

        except:
            print('Erro. Digite apenas números inteiros para idade.')

    soma_idades += dados['idade']
    pessoas.append(dados.copy())

    while True:
        resp = input('Quer continuar? [S/N]: ').upper()[0]

        if resp in 'SN':
            break
        print('Erro. Digite apenas S ou N.')

    if resp == 'N':
            break

print('-'*40)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
media_idade = soma_idades/len(pessoas)
print(f'A média de idade das pessoas cadastradas é {media_idade:.1f} anos')

print('As mulheres cadastradas foram ', end='')

for i in pessoas:
    if i['sexo'] == 'F':
        print(f'{i["nome"]} ', end='')
print()

print('As pessoas com idade maior que a média: ', end='')
for i in pessoas:
    if i['idade'] >= media_idade:
        print(f'{i["nome"]}', end=' - ')
