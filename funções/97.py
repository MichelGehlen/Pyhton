def escreva(x):
    tam = len(x)+4
    print("-"*tam)
    print(f'  {x}')
    print("-"*tam)


texto = str(input("Digite um texto: "))
escreva(texto)