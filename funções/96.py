def area(l,c):
    area = l*c
    print(f"A área de um terreno {l}x{c} é de {area}m")


print('Controle de Terrenos'.center(30))
print("-"*30)
l = float(input("Largura: "))
c = float(input("Comprimento: "))
area(l,c)