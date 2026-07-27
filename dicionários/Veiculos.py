garagem = []
while True:
    carro = {}
    carro['Modelo'] = str(input("Modelo: "))
    carro['Ano'] = int(input("Ano: "))
    carro['Km'] = int(input("Km: "))
    garagem.append(carro.copy())
    r = str(input("Deseja continuar? [S/N]: ")).upper().strip()[0]
    if r not in 'SN':
        print("!Erro responda com S/N")
        r = str(input("Deseja continuar? [S/N]: "))
    if r == 'N':
        break

mais_velho = garagem[0]
mais_novo = garagem[0]
for p in garagem:
    if mais_velho['Ano'] > p['Ano']:
        mais_velho = p
    if mais_novo['Ano'] < p['Ano']:
        mais_novo = p

soma = 0
for s in garagem:
    soma += (s['Km'])
media = soma / len(garagem)

print("=-"*30)
print(f"RELATORIO GARAGEM".center(60))
print("=-"*30)
print(f'{'Modelo':<10}{'Ano':<10}{'Km':<10}')
for p in garagem:
    print(f'{p['Modelo']:<10}{p['Ano']:<10}{p['Km']:<10}')
print(' ')
print("O carro mais novo é: ")
print(mais_novo)
print("O carro mais velho é: ")
print(mais_velho)
print(f"A media de quilometragem é {media:.2f}")