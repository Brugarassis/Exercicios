'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade 
de gols feitos em cada partida.No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.
'''

dados = {}

dados['Nome'] = input('Nome do jogador: ')
dados['Partidas'] = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
total = 0
for i in range(1, dados['Partidas'] + 1):
    gol = int(input(f'Quantos gols ele fez na partida {i}: '))
    total += gol

dados['Qtd.gols'] = total 

for k, v in dados.items():
    print(f'{k} = {v}')


