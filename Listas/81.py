valores = []
resp = 'S'

while resp == 'S':
    valores.append(int(input("Digite um valor: ")))
    resp = str(input('Deseja adicionar outro valor? [S/N]  ')).upper()
    while resp not in 'SN':
        resp = str(input('Responda apenas com [S/N]: ')).upper()

print(f"Essa lista tem {len(valores)} numeros")
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('o valor 5 faz parte da lista!')
else:
    print('o valor 5 não faz parte da lista')