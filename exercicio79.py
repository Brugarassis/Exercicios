'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores 
numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
'''

numbers = []

while True:
    number = int(input('Adicione um número a lista: '))

    if number not in numbers:
        numbers.append(number)
        print('Valor adicionado com sucesso.')

    else:
        print('Esse valor já foi adicionado a lista anteriormente.')

    exit = input('Terminou sua lista? Digite [C] para continuar ou [S] para sair.').strip().upper()

    if exit == 'S':
        break

    
    
print(sorted(numbers))