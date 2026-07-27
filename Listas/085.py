
n = [[], []]
valor = 0

for c in range(1,7):
    valor = int(input('Digite um valor: '))
    if valor %2 == 0:
        n[0].append(valor)
    else:
        n[1].append(valor)
print('-='*40)
print(f'Numeros pares {n[0]}')
print(f'Numeros impares {n[1]}')
