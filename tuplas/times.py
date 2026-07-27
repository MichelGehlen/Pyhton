
times = ('Flamengo', 
         'Palmeiras', 
         'Cruzeiro', 
         'Mirassol', 
         'Fluminense', 
         'Bahia', 
         'Botafogo', 
         'São Paulo', 
         'Corinthians', 
         'Red Bull Bragantino', 
         'Grêmio', 
         'Vasco', 
         'Athletico-PR', 
         'Santos', 
         'Remo', 
         'Coritiba', 
         'Atlético-MG', 
         'Juventude', 
         'Goiás',
         'Fortaleza')

print(f"Os cinco primeiros colocados são: {times[0:5]}: ")
print(f"Os ultimos quatro colocados são: {times[-4:]}")
print(f"Em ordem alfabetica: {sorted(times)}")
print(f"Gremio esta na posição: {times.index("Grêmio")}")
