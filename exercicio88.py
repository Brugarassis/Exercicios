'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar 
palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep

mega = []
lista = []

jogos = int(input(f'  Quantos jogos você deseja fazer?   '))
print('-' * 40)

total_jogos = 0
while total_jogos < jogos:
    cont = 0
    while True:
        numero = randint(1, 61)
        if numero not in lista:
            lista.append(numero)
            cont += 1

        if cont >= 6:
            break

    total_jogos +=1

    mega.append(lista[:])
    lista.clear()

for i, j in enumerate(mega):
    print(f'Jogo {i + 1}:   {sorted(j)}')
    sleep(1)
    print('-' * 40)

    





