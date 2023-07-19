'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores 
numéricos e cadastre-os em uma lista única que mantenha separados os valores 
pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

numbers = []
pares = []
impares = []

for i in range(0, 7):
    number = int(input('Digite um número: '))

    if number % 2 == 0:
        pares.append(number)
    
    else:
        impares.append(number)
       

numbers.append(pares[:])
numbers.append(impares[:])

print(numbers)
print(sorted(numbers[0]))
print(sorted(numbers[1]))


    

