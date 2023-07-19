# média dos bimestres

nota_1 = input('Digite a nota do primeiro bimestre: ')
nota_2 = input('Digite a nota do segundo bimestre: ')
nota_3 = input('Digite a nota do terceiro bimestre: ')
nota_4 = input('Digite a nota do quarto bimestre: ')

nota_1_float = float(nota_1)
nota_2_float = float(nota_2)
nota_3_float = float(nota_3)
nota_4_float = float(nota_4)

media = (nota_1_float + nota_2_float + nota_3_float + nota_4_float)/4

print(f'A sua média anual foi de {media:.2f}')
