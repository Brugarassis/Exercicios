'''
Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
Olá, Mundo!
~~~~~~~~~
'''

def escreva(a):
    print('~' * (len(a) +4))
    print(f'  {a}')
    print('~' * (len(a) + 4))

escreva('Bruno Top')