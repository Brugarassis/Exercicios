'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

maior = 0
menor = 0
for i in range(1,6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    
    if i == 1:
        maior = peso
        menor = peso
    
    else:
        if peso > maior:
            maior = peso

        if menor > peso:
            menor = peso
print(f'O maior peso é {maior:.3f}kg')
print(f'O menor peso é {menor:.3f}kg')
    
