'''
Exercício Python 054: Crie um programa que leia 
o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
'''

from datetime import date
c = 0
c2 = 0
ano_atual = date.today().year

for i in range(0, 7):
    ano_nascimento = int(input('Digite o ano que você nasceu: '))

    if ano_atual - ano_nascimento >= 18:
        c += 1
    else:
        c2 += 1

if c == 0:
    print('Nenhuma pessoa atingiu a maoir idade.')

elif c2 == 0:
    print(f'Todas as pessoas atingiram a maior idade.')

else:
    print(f'{c} pessoas já atigiram a maior idade, enquanto que {c2}, ainda não.')
