'''
Exercício Python 057: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado, 
peça a digitação novamente até ter um valor correto.
'''

while True:
    print('Qual o seu sexo?')
    sexo = input('Digite [M] para masculino e [F] para feminino: ').strip().upper()

    if sexo not in 'FM':
        print('Digite apenas [M] ou [F]')
        continue
    
    if len(sexo) > 1:
        print('Digite apenas um dos sexos.')
        continue
    else:
        break

if sexo == 'M':
    print('Masculino')

else:
    print('Feminino')

