'''
Exercício Python 075: Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

number_1 = int(input('Digite um número: '))
number_2 = int(input('Digite um número: '))
number_3 = int(input('Digite um número: '))
number_4 = int(input('Digite um número: '))

numbers = (number_1, number_2, number_3, number_4)

print(f' O número 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O número 3 apereceu pela primeira vez na posição {numbers.index(3)}')
else:
    print('Você não digitou nenhum 3.')
print('Os números pares que você digitou foram: ', end='')

for i in numbers:
    if i % 2 == 0:
        print(f'{i}  ', end='')