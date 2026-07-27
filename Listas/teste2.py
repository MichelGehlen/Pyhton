valores = []
for cont in range(0, 5): #para o usuario digitar os valores da lista
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores): #pega o indice junto
    print(f'Na posicao {c} tem o valor {v}...')