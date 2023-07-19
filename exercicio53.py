'''
Exercício Python 053: Crie um programa que leia uma
frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
'''
frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = '-'.join(palavras)

inverso = ''

for i in junto[::-1]:
    inverso += i

print(inverso)

if junto == inverso:
    print('Essa frase é um palíndromo')
else: 
    print('Essa frase não é um palíndromo')
    