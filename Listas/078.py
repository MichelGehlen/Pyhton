valores = []
for cont in range(0, 5): #para o usuario digitar os valores da lista
    valores.append(int(input(f"Digite um valor para a posição {cont}: ")))

maior = valores[0]
menor = valores[0]
print(f'Você digitou os valores {valores}')
for i in range(len(valores)):
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]
print(f'O maior valor digitado foi {maior} nas posições', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')

print()
print(f'O menor valor digitado foi {menor} ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')

