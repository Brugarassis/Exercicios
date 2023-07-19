'''
Exercício Python 076: Crie um programa que tenha uma tupla única 
com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

compras = ('Chopp', 12.9,
          'Caipirinha', 20,
          'Batata frita', 23.5,
          'Asa de frango', 38.7,
          'Refri lata', 5,
          'Água', 3.5)

print('-'* 40)
print(f'{"Cardápio - Bar":^40}')
print('-'* 40)
 
for i in range(0, len(compras)):
    if i % 2 == 0:
        print(f'{compras[i]:.<30}', end='')
    else:
        print(f'{compras[i]:>7.2f}')

