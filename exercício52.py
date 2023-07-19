# números primos

number = int(input('Digite um número: '))

c=0

for i in range (1, number+1):
    if number % i == 0:
        c += 1
        print(f'O {number} é divisível por {i}')

if number == 1:
        print('O número 1 não é primo.')   
elif c >= 3:
            print(f'O número {number} não é primo.')
else:
            print(f'O número {number} é primo.')