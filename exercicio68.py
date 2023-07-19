'''
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
'''
from random import randint
i = 0

while True:
    computer_number = randint(1, 6)
    print(computer_number)
    par_impar = input('Par [P] ou impar [I]  ').strip().upper()
        

    number = int(input('Escolha um número para jogar: '))
    soma = computer_number + number

    if soma % 2 == 0:
        if par_impar == 'P':
            print('Parabéns, você ganhou!!!')
            i += 1

        elif par_impar == 'I':
            print('Você perdeu!')
            break
        else:
            print('Digite apenas [P] para par ou [I] para impar')
            
    else:
        if par_impar == 'I':
            print('Parabéns, você ganhou!!!')
            i += 1

        elif par_impar == 'P':
            print('Você perdeu!')
            break
        else:
            print('Digite apenas [P] para par ou [I] para impar')
            continue

print(f'Você teve {i} vitórias consecutivas.')

    







