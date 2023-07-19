number = int(input('Digite um número: '))
razao = int(input('Qual a razão da sua PA? '))
i=1
termos = 0
plus = 10

while plus != 0:
    termos = termos + plus 
    while i <=termos:
        print(f'{number} -> ', end='')
        number = number + razao
        i += 1
    print('Pausa')
    plus = int(input('Quantos termos você quer mostrar a mais? '))
    continue
print(f'Progressão finalizada com {termos} mostrados.')
print('Fim')