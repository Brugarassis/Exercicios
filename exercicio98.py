'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar 
três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep

def contador(i, f, p):
    
    if p < 0:
        p = p *(-1)
    x = i
    if f > i:
        while x <= f:
            print(f'{x} - ', end='')
            x += p
            sleep(0.5)

    else:
        while x >= f:
            print(f'{x} - ', end='')
            x -= p
            sleep(0.5)
    print('Fim')

contador(1, 10, 1)   
contador(10, 0, 2)
contador(25, 0, 5)