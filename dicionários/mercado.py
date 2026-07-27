produtos = list()
while True:
    produto = {}
    produto['Nome'] = str(input("Produto: "))
    produto['Preço'] = float(input("Preço: "))
    produto['Quantidade'] = int(input("Quantidade: "))
    produtos.append(produto.copy())
    r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while r not in 'SN':
        print("ERRO! responda com S/N")
        r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if r == 'N':
        break

soma_precos = 0
for p in produtos:
    soma_precos += p['Preço']

media = soma_precos / len(produtos)

print("-="*30)
for p in produtos:
    print(f'{p["Nome"]:<15} R${p["Preço"]:>7.2f}  Qtd:{p["Quantidade"]}')
print(f"Total gasto: R${soma_precos:.2f}")
print(f"A média dos produtos é R${media:.2f}")
maior = produtos[0]
menor = produtos[0]
for i in produtos:
    if i['Preço'] > maior['Preço']:
        maior = i
    if i['Preço'] < menor['Preço']:
        menor = i
    
print(f'O Produto mais caro é {maior["Nome"]} que custa R${maior["Preço"]:.2f}')
print(f'O Produto mais barato é {menor["Nome"]} que custa R${menor["Preço"]:.2f}')


        
