pessoas = []

while True:
    pessoa = {}

    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa.copy())

    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('-' * 30)

for p in pessoas:
    print(f'Nome: {p["nome"]} | Idade: {p["idade"]}')