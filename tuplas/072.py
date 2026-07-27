extenso = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete'
)

while True:

    n = int(input("Digite um número: "))

    if 0 <= n <= 7:

        print(extenso[n])

        resposta = input("Deseja continuar? (s/n): ")

        if resposta == "n":
            break

    else:
        print("Número inválido")