number = int(input('Digite o primeiro número da progressão: '))
razao = int(input('Digite a razão da progressão: '))

for i in range(0, 10):
    print(number, end='   ')

    number += razao
    
print('Fim')