# Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

def area_retangulo(c, l):
    a = c * l
    print(f'A área de um terreno de {c} x {l} é de {a:.2f} m².')
    

print('Terreno')
print('-'*30)
c = float(input('Comprimento (m): '))
l = float(input('Largura (m): '))

area_retangulo(c, l)