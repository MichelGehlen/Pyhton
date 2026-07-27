matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()
total = 0
maior = 0
for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = int(input('Digite o valor: '))
        if matriz [c][i] % 2 == 0:
            pares.append(matriz[c][i])
        if i == 2:
            total += matriz[c][i]
        if c == 1:
            if i == 0:
                maior = matriz[c][i]
            elif maior < matriz[c][i]:
                maior = matriz[c][i]
                

for c in range (0,3):
    for i in range(0,3):
        print(f'[{matriz[c][i]}]',end='')
    print()

print(f'A soma dos numeros {pares} é {sum(pares)}')    
print(f'A soma dos valores da terceira linha é {total}')
print(f'O maior valor da segunda linha é {maior}')