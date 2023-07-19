# metros em centímetros
medida_metro = input('Digite o valor em metros que deseja converter: ')
medida_metro_float = float(medida_metro)

medida_centimetro = medida_metro_float * 100
medida_centimetro_int = int(medida_centimetro)

print(f'Valor convertido: {medida_centimetro_int} centimetros')

'''
from random import randint
mega = []

for i in range(0, 6):
    luck_number = randint(1, 61)
    mega.append(luck_number)
'''