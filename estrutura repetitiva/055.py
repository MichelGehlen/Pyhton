
for c in range (1, 6):
    peso = float(input(f"Digite o pesso da {c} pessoa: "))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print("O maior peso foi {:.2f}".format(maior_peso))
print("O menor peso foi {:.2f}".format(menor_peso))

