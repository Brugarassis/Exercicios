'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = {}

aluno['nome'] = input('Nome do aluno: ')
aluno['media'] = float(input('Qual a média desse aluno? '))

print(f'O nome do aluno é {aluno["nome"]}')
print(f'Sua média foi {aluno["media"]}.')

if aluno['media'] >= 6:
    print('Aluno aprovado')

else:
    print('Aluno em recuperação.')