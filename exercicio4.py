from datetime import date

ano = input('Digite o ano que você deseja analizar: ')
ano_int = int(ano)

if ano_int == 0:
    ano_int = date.today().year
    print(ano_int)
if ano_int % 100 == 0:
    print('Esse ano não é bissexto')

elif ano_int % 4 == 0:
    print('Esse ano é bissexto')

else:
    print('Esse ano não é bissexto')


