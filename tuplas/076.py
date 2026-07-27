listagem = ('Lápis', 1.72,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25)

for i in range(len(listagem)):

    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end='')
    else:
        print(f'R${listagem[i]:>.2f}')