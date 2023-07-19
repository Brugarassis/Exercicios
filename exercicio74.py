'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e 
também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

number_1 = randint(0, 100)
number_2 = randint(0, 100)
number_3 = randint(0, 100)
number_4 = randint(0, 100)
number_5 = randint(0, 100)

numbers = (number_1, number_2, number_3, number_4, number_5)

print(numbers)
print('-'*60)
print(sorted(numbers))
print('-'*60)
print(f'O menor número na tupla é o {sorted(numbers)[0]}')
print(f'O maior número na tupla é o {sorted(numbers)[-1]}')


# poderia usar as funçoes max e min.

