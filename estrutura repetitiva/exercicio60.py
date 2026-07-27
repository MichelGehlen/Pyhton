
soma = 0
for c in range(1,7):
    x = int(input("Digite um numero: "))
    if x % 2 == 0:
        soma = soma + x
print('A soma dos numeros pares é igual a {}'.format(soma))
