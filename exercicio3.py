# peso e altura ideal

# formula peso - (72.7*altura) - 58
# formula altura - Para homens: (72.7*h) - 58
#                  Para mulheres: (62.1*h) - 44.7
"""
altura = input('Digite sua altura: ')
altura_float = float(altura)
peso_ideal = (72.7 * altura_float) - 58

print(f'O seu peso ideal é de: {peso_ideal:.3f} kg')
"""
while True:
    sexo = input('Se for homem digite "h", e se for mulher "m - ')
    sexo_permitido = 'hm'

    if sexo not in sexo_permitido:
         print('Operador inválido.')
         continue
    if len(sexo) > 1:
         print('Digite apenas uma letra.')
         continue
    while True:
        altura = input('Digite sua altura: ')
        altura_float = 0
        altura_valida = None

        try:
             altura_float = float(altura)
             altura_valida = True
       
        except:
             altura_valida = None
    
        if altura_valida is None:
            print('Digite apenas números.')
            continue
        break
    
    if sexo == 'h':
         peso_ideal_h = (72.7 * altura_float) - 58
         print(f'Seu peso ideal é de: {peso_ideal_h:.3f}kg')

    else:
         peso_ideal_m = (62.1 * altura_float) - 44.7
         print(f'Seu peso ideal é de: {peso_ideal_m:.3f}kg')
    break
    
print('acabou')


