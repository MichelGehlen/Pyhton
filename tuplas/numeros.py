n = (int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")))

print(f"Voce digitou os valores: {n}")
print(f"O numero 9 apareceu {n.count(9)} vezes")
if 3 in n:
    print(f"O numero 3 esta na posição {n.index(3)}")
else:
    print("Não tem numero 3 na tupla")

print("Numeros pares: ")
for i in n:
    if i % 2 == 0:
        print(i)

