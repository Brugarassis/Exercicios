'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham 
resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2' : randint(1, 6),
        'Jogador 3' : randint(1, 6),
        'Jogador 4' : randint(1, 6)}

raking = []

print('Valores sorteador por cada jogador')
print()
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

raking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
print()
print('Ranking dos Jogadores')

for i, v in enumerate(raking):
    print(f'{i + 1}º Lugar - {v[0]} que tirou {v[1]}')
    sleep(1)
    print()




'''
jogadores = {}
lista = []

for i in range(0, 4):
    jogadores['Jogador'] = f'Jogador {i + 1}'
    jogadores ['Dado'] = randint(1, 6)
    lista.append(jogadores.copy())

print(lista)

'''