'''
Exercício Python 060: Faça um programa 
que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

number = int(input('Que número você deseja fatorar?   '))
i = number
mult = 1

print(f'Calculando {i}! ...', end='')
while i > 0:
    print(f'{i}', end='')
    print(f'x'if i > 1 else '=', end='')
    mult *= i
    i -= 1

print(mult)
    