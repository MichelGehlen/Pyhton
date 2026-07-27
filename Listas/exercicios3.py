valores = []
for cont in range(0, 5): #para o usuario digitar os valores da lista
    valores.append(int(input("Digite um valor: ")))

maior = valores[0]
for i in range (len(valores)):
    if maior < valores[i]:
        maior = valores[i]

print(f'o maior valor é {maior}')
print(f'Posições: ',end=' ')

for c, v in enumerate(valores):
    if v == maior:
        print(f'{c} e ', end='')