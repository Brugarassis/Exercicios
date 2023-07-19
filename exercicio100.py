'''
Exercício Python 099: Faça um programa que tenha uma função chamada 
maior(), que receba vários parâmetros com valores inteiros. Seu programa 
tem que analisar todos os valores e dizer qual deles é o maior.
'''

def maior(*args):
    lista = []
    for i in args:
        lista.append(i)
    print('Analizando valores passados...')
    print(f'{lista}. Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {sorted(lista)[-1]}')


maior(1, 2, 44, 55, 39, 200, 349 , -1, -2)
