valores = []
valores_pares = []
valores_imapres = []
resp = 'S'

while resp == 'S':
    n = (int(input("Digite um valor: ")))
    resp = str(input('Deseja adicionar outro valor? [S/N]  ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Responda apenas com [S/N]: ')).strip().upper()[0]
    if n % 2== 0:
        valores_pares.append(n)
    else:
        valores_imapres.append(n)
    valores.append(n)

print('=-'*30)
print(f"A lista completa é {valores}")
print(f'A lista de valores pares é {valores_pares}')
print(f'A lista de valores impares é {valores_imapres}')