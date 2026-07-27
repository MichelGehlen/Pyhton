n = (int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")),
int(input("Digite um numero: ")))

maiores = n[0]

for i in range(len(n,3)):
    if n[i] > maiores:
        posicao = i
        maiores = n[i]
        print(f"Maior valor {maiores}")
    