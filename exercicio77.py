'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras 
(não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

nomes = ('Bruno', 'Romulo', 'Gabi', 'Walfredo', 'Rosane', 'Rhaissa', 'Emely')

for i in nomes:
    print(f'\n Na palavra {i}, exixtem ', end='')
    for l in i:
        if l.lower() in 'aeiou':
            print(l, end=' ')

