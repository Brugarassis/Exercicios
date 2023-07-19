'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. 
'''

while True:
    number = int(input('Qual número você deseja saber a tabuada:   '))

    if number <= 0:
        print('Fim')
        break

    for i in range(1, 11):
        print(f'{i} x {number} = ', i * number)
