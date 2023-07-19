'''
Exercício Python 084: Faça um programa que leia nome e peso de 
várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pessoas = []

i = 0
pesado = 0
leve = 0

while True:
    nome = input('Nome: ')
    peso = float(input('Peso:  '))
    i += 1

    if pesado < peso:
        pesado = peso

    if leve == 0:
        leve = peso

    elif leve > peso:
        leve = peso
    
    pessoas.append(nome)
    pessoas.append(peso)

    continuar = input('Deseja continuar?  [S/N]:  ').strip().upper() 

    if continuar == 'N':
        break

print(f'Você cadastrou {i} pessoas.')

print(pessoas)
print(len(pessoas))


print(f'O maior peso foi de {pesado:.2f}kg. O peso de ', end='')
for c, p in enumerate(pessoas):
    if p == pesado:
        print(pessoas[c-1], end='  ')

print()
 
print(f'O menor peso foi de {leve:.2f}kg. O peso de ', end='  ')
for c, p in enumerate(pessoas):
    if p == leve:
        print(pessoas[c-1], end='  ')


