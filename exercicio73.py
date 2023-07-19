'''
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da internacional.
'''
Classificacao = ('Botafogo', 'Flamengo','Grêmio', 'Fluminense', 'Palmeiras',
                'Bragantino', 'Fortaleza', 'São Paulo', 'Cruzeiro', 'Internacional',
                'Athletico-PR','Atlético-MG', 'Santos', 'Cuiabá', 'Corinthians', 'Bahia',
                'Goiás', 'Coritiba', 'Vasco', 'América-MG')

print('-'*60)

print(Classificacao[0:5])

print('-'*60)

print(Classificacao[-4:])

print('-'*60)

print(sorted(Classificacao))

print('-'*60)

print((Classificacao.index('Internacional') + 1))
 
