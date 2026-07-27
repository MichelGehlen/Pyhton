produtos = (
    'Saco', 1.75,
    'Lápis', 2.00,
    'Detergente', 10.00,
    'Rolo', 30.00
)

for i in range(0, len(produtos)):

    if i % 2 == 0:
        print(f'{produtos[i]:30}', end="")

    else:
        print(f'R$ {produtos[i]:.2f}')