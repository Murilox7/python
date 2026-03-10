time = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 
         'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 
         'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print('Os primeiros 5 times são: ')
print(time[0:5])
print('=-'*15)
print('Os ultimos 4 times são: ')
print(time[16:20])
print('=-'*15)
print(f'Times em ordem alfabetica {sorted(time)}')
print('=-'*15)
print(f'O Bahia esta na {time.index("Bahia")+1} posição')