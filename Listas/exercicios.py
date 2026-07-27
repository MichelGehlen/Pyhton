valores = []
for cont in range(0, 8): #para o usuario digitar os valores da lista
    valores.append(int(input("Digite um valor: ")))

soma = sum(valores)
media = soma / len(valores)

print(f'você digitou os valores {valores}')
print(f'A soma total dos numeros é {soma}')
print(f'E a média entre eles é {media}')
    