valores = []
resp = 'S'

while resp == 'S':

    numero = int(input('Digite um valor: '))

    if numero in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(numero)
        print('Valor adicionado com sucesso!')

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

print("=-" * 30)
print(f'Você digitou os valores {valores}')