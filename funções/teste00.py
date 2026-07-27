def formatar(x):
    print('=-'*30)
    print(f"{x}".center(60))
    print("=-"*30)


carro = dict()
garagem = list()
formatar("ALUGUEL")
while True:
    carro['Modelo'] = str(input("Modelo: "))
    carro['Ano'] = int(input("Ano: "))
    carro['Km'] = int(input("Km: "))
    garagem.append(carro.copy())
    r = str(input("Adicionar mais um? [S|N] ")).upper().strip()[0]
    while r not in "SN":
        print("Responda com [S|N]")
        r = str(input("Adicionar mais um? [S|N] ")).upper().strip()[0]
    if r == "N":
        break

formatar("DADOS")
print("cod ",end='')
for i in carro.keys():
    print(f"{i:<15}",end='')
print()
print("-"*40)
for k,v in enumerate(garagem):
    print(f"{k:<5}",end='')
    for d in v.values():
        print(f"{str(d):<15}",end='')
    print()
print('-'*40)

formatar("BUSCA")
while True:
    busca = int(input("Cod: "))
    if 0 <= busca < len(garagem):
        carro_encontrado = garagem[busca]
        for k,v in carro_encontrado.items():
            formatar({k})
            print(f'{k}:{v}')
    else:
        print("Carro não encontrado")
    r = str(input("Continuar [S|N] ")).upper().strip()[0]
    if r == 'N':
        break
