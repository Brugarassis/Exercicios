'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média 
de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
alunos = []
lista = []

while True:
    nome = input('Nome do aluno: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2)/ 2

    lista.append(nome)
    lista.append(nota_1)
    lista.append(nota_2)
    lista.append(media)

    alunos.append(lista[:])
    lista.clear()
    print()

    add = input('Deseja adicionar mais algum aluno? [S]/[N]}'). strip().upper()

    if add == 'N':
        break
print()
print()
for i, m in enumerate(alunos):
    print(f'{i:<5}. {m[0]:<10} --- Média = {m[3]:>8.1f}')
print()
print()

while True:
    entrada_nota = int(input('Deseja ver a nota de qual aluno? (Digite 999 para sair do programa.)  '))

    if entrada_nota == 999:
        print('Saiu')
        break

    if entrada_nota < len(alunos):
        print(f'Notas de {alunos[entrada_nota][0]} são {alunos[entrada_nota][1]} e {alunos[entrada_nota][2]} ')

    else:
        print('Digite um índice válido.')
    
