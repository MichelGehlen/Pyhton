valores = []
pares = []
impares = []
for cont in range(0,10):
    valores.append(int(input('Digite um valor: ')))

for i in valores:
    if valores[i] % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)

print(f'Lista de numeros pares {pares}')
print(f'Lista de numeros impar {impares}')
        