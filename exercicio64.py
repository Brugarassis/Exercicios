'''
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
i = 0
soma = 0

while True:
    number = int(input('Digite 999 para parar, ou outro que deseja somar: '))
    
    if number != 999:
        soma += number
        i +=1
        continue
    else:
        break
print(f'A soma dos {i} termos é {soma}')