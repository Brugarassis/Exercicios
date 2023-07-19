'''
Exercício Python 086: Crie um programa que declare uma 
matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''

numbers = [[], [], []]


for i in range(0, 9):
    number = int(input('Digite um número: '))
    if i < 3:
        numbers[0].append(number)
    elif  2 < i < 6:
        numbers[1].append(number)
    else:
        numbers[2].append(number)

  
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{numbers[l][c]:^5}]', end='')
    print()
