'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

lista = []
par = []
impar = []

while True:
    n = int(input('Adicione um valor: '))
    lista.append(n)

    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

    exit = input('Deseja adicionar mais valores? - Enter para continuar e [S] para sair.').strip().upper()

    if exit == 'S':
        print('Fim da lista')
        break
    

print(sorted(lista))
print(sorted(par))
print(sorted(impar))





