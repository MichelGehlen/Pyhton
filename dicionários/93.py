jogador = dict()
gols_partidas = list()  # Lista para os gols de CADA jogador
time = list()           # Lista principal para guardar TODO O TIME

while True:
    gols_partidas.clear() # Limpa os gols para o próximo jogador
    jogador['Nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

    for c in range(0, tot):
        gols_partidas.append(int(input(f'Quantos gols na partida {c+1}? '))) # c+1 fica mais natural pro usuário (Partida 1, 2...)
    
    jogador['gols'] = gols_partidas[:]
    jogador['total'] = sum(gols_partidas)

    # Guarda uma cópia do jogador atual dentro do time
    time.append(jogador.copy())

    r = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
    while r not in 'SN':
        print('Apenas S/N !!')
        r = str(input("Quer continuar: [S/N]: ")).upper().strip()[0]
    if r == 'N':
        break

print('-=' * 30)

# Cabeçalho da tabela
print(f'{"Cod":<5}{"Nome":<15}{"Gols":<15}{"Total":<5}')
print('-' * 40)

# O laço FOR correto: 'i' é o código/índice (0, 1, 2...) e 'j' é o dicionário do jogador
for i, j in enumerate(time):
    print(f'{i:<5}{j["Nome"]:<15}{str(j["gols"]):<15}{j["total"]:<5}')

print("-"*30)
p = 0
while p != 990:
    p = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if 0 <= p <len(time):
        print(f'Nome:{time[p]["Nome"]} Gols:{time[p]["gols"]} Total:{time[p]["total"]}')
    elif p !=999:
        print("Não encontrado")