dados = []
pessoas = []

while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))

    pessoas.append(dados[:])
    dados.clear()

    r = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break

maior = pessoas[0][1]
menor = pessoas[0][1]

for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maior}kg. Peso de ', end='')

for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi {menor}kg. Peso de ', end='')

for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')