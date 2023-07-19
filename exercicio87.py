'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
numbers = [[], [], []]
spar = 0
soma_c3 = 0

for i in range(0, 9):
    number = int(input('Digite um número: '))
    if i < 3:
        numbers[0].append(number)
    elif  2 < i < 6:
        numbers[1].append(number)
    else:
        numbers[2].append(number)
  
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{numbers[l][c]:^5}]', end='')
        if numbers [l][c] % 2 == 0:
            spar += numbers[l][c]
    print()

for l in range(0, 3):
    soma_c3 += numbers [l][2]

numbers[1].sort()

print(f'A soma dos números pares da matriz é {spar}')
print(f'A soma dos valores da terceira coluna é {soma_c3}')
print(f'O maior número da segunda linha é {numbers[1][-1]}')

