'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

numbers = []

for i in range(0, 5):
    numbers.append(int(input(f'Digite um número para a posição {i}:  ')))

print(f'Lista - {numbers}')
print()

for i, number in enumerate(numbers):
    if number == min(numbers):
        print(f'O menor número da lista é o {number}, que está na posição {i}')

    if number == max(numbers):
        print(f'O maior número da lista é o {number}, que está na posição {i}')
        




