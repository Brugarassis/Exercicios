'''
Exercício Python 080: Crie um programa onde o usuário possa digitar 
cinco valores numéricos e cadastre-os em uma lista, já na posição correta 
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

numbers = []

for i in range(0,5):
    number = int(input('Adicione um valor: '))

    if i == 0 or number > numbers[-1]:
        numbers.append(number)
        print('Adicionado ao final da lista...')
    
    else:
        p = 0
        while p < len(numbers):
            if number <= numbers[p]:
                numbers.insert(p, number)
                print(f'Adicionando na posição {p}...')
                break
            p +=1
print()
print()
print(f'A lista ordenada é: {numbers}')


        


    





    
   

