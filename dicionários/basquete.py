jogador = dict()
time = list()
pontos = list()
while True:
    pontos.clear()
    jogador['Nome'] = str(input('Nome: '))
    tot = int(input("Quantidade de partidas: "))

    for c in range(0, tot):
        pontos.append(int(input(f'Quantos pontos na partida {c+1}? ')))

    jogador['Cesta'] = pontos[:]
    jogador['Total'] = sum(pontos)

    time.append(jogador.copy())

    r = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    while r not in 'SN':
        print('Apenas S/N !!')
        r = str(input("Quer continuar: [S/N]: ")).upper().strip()[0]
    if r == 'N':
        break

stats_mai = time[0]
stats_men = time[0]
for c in time:
    if c['Total'] > stats_mai['Total']:
        stats_mai = c
    if c['Total'] < stats_men['Total']:
        stats_men = c

print("-="*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("-"*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

r = 0
while r != 999:
    r = int(input("Mostrar dados de qual jogador? "))
    if 0 <= r <len(time):
        print(f"Nome:{time[r]['Nome']}\nPontos:{time[r]['Cesta']}\nTotal:{time[r]['Total']}")
    elif r != 999:
        print("Não encontrado")
print("=-"*30)
print(f'Menor pontuação: {stats_men["Nome"]} - {stats_men["Total"]} pontos')
print(f'Maior pontuação: {stats_mai["Nome"]} - {stats_mai["Total"]} pontos')
