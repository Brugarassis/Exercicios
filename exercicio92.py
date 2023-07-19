'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira 
de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for 
diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import datetime

dados = {}

nome = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
idade = datetime.now().year - ano_nascimento
dados['Nome'] = nome
dados['Idade'] = idade

dados['ctps'] = int(input('Carteira de Trabalho (Digite 0 caso não possua):  '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Qual o ano de contratação? '))
    dados['salário'] = int(input('Qual seu salário? '))
    dados['aposentadoria'] = dados['Idade'] + (dados['contratação'] + 35 - datetime.now().year)
print('-'*30)

for k, v in dados.items():
    print(f'{k} = {v}')