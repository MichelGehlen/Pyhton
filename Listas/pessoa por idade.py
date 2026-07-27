dados = list()
pessoas = list()
soma = 0
while True:
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break

print('-='*30)
print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f'A pessoa mais velha é ', end='')
for c in pessoas:
    if mai == c[1]:
        print(c[0])
print(f'A pessoa mais nova é ', end='')
for c in pessoas:
    if men == c[1]:
        print(c[0])


soma = sum(c[1] for c in pessoas)
media = soma / len(pessoas)

print(f"A media de idades é {media}")
