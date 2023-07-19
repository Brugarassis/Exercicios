'''
Faça um programa que tenha uma lista chamada números e
duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
 a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteia(lista):
    for i in range(0, 5):
        numero = randint(0, 10)
        numeros.append(numero)
    print(sorted(numeros))

def soma_par(lista):
    soma = 0
    for i in lista:
       if i % 2 ==0:
        soma += i
    print(f'A soma dos pares é de {soma}.')

numeros = []
sorteia(numeros)
soma_par(numeros)