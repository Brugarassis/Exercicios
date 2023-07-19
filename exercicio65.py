'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

soma = 0
i = 0
maior = 0
menor = 0

while True:
    number = int(input('Digite o número que deseja adicionar: '))
    close = input('Deseja continuar adicionando valores? Se não, digite [N]').strip().upper()
    soma += number

    if number > maior:
        maior = number
    
    if i == 0:
        menor = number
    else:
        if number < menor:
            menor = number
    i += 1

    if close == 'N':
        break
    else:
        continue

print(f'Você digitou {i} valores e a média entre eles foi de {soma / i} ')
print(f'O maior valor foi o {maior} e o menor o {menor}')

