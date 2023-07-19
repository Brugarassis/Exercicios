'''
Exercício Python 081: Crie um programa que vai ler vários 
números e colocar em uma lista. Depois disso, mostre:

A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
i = 0

while True:
    number = int(input('Adicione um valor: '))
    lista.append(number)
    i += 1

    exit = input('Deseja continuar adicionando valores a lista? [S] para sim, [N] para não. ').strip().upper()

    if exit == 'N':
        print('Fim da lista.')
        break

    else:
        continue
    
    
lista.sort(reverse=True)
print(f' Lista ordenada de forma decrescente -> {lista}')
print(f'Você digitou {i} números.')

if 5 in lista:
    print('O número 5 foi digitado e esta na lista.')
else:
    print('O número 5 não está na lista.')







