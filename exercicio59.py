'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

while True:
    number_1 = input('Primeiro valor: ')
    number_2 = input('segundo valor: ')
    
    number_1_float = 0
    number_2_float = 0
    valid_number = None

    try:
        number_1_float = float(number_1)
        number_2_float = float(number_2)
        valid_number = True
    
    except:
        valid_number = None
        print('Primeiro ou segundo valor inválidos, por favor digite apenas números.')
        continue
    
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair do programa')

    options = None

    while options != '5':
        
        options = input('Selecione uma das opções: ')
        valid_options = '12345'

        if options  not in valid_options:
            print('Opção inválida')
            continue

        if len(options) > 1:
            print('Opção inválida')
            continue

        if options == '1':
            sum = number_1_float + number_2_float
            print(f'A soma dos dois números é igual a: {sum:.2f}')
            continue
        
        elif options == '2':
            multiplication = number_1_float * number_2_float
            print(f'A multiplicação dos dois números é igual a: {multiplication:.2f}')
            continue

        elif options == '3':

            if number_1_float > number_2_float:
                print(f'O número {number_1_float} é maior que o {number_2_float}')
                continue
            
            elif number_1_float < number_2_float:
                print(f'O número {number_1_float} é menor que o {number_2_float}')
                continue
            
            else:
                print('Os dois números são iguais.')
                continue

        elif options == '4':
            print('Informe os números novamente.')
            break
        continue
    else:
        print('Você fechou o programa.')
        break
        
            
        


    

    
    

        
    
        
    


        
            

