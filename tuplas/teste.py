lanche = ("hamburguer", "suco", "pizza", "pudim", "batat frita")

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for pos,comida in  enumerate (lanche):
    print(f'eu vou comer {comida}, na posição {pos}')

for comida in lanche:
    print(f'Eu vou comer {comida}')