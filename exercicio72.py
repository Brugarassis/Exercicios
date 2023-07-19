'''
Exercício Python 072: Crie um programa que tenha uma dupla totalmente 
preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
numbers = ('zero', 'um', 'dois', 'três', 'Quatro', 'Cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    entrada = int(input('Escolha um número de 0 a 20: '))

    if entrada > 20:
        print('Tente novamente. ', end='')
    
    elif entrada < 0:
        print('Digite apenas números positivos. ', end='')
    
    else:
        print(f'Você digitou o número {numbers[entrada]}.')
        break