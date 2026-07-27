from random import randint
from time import sleep
lista = list()
def sorteio(x):
    """sorteio
    --Sorteia uma quantidade de números aleatórios sem repetição.

    Args:
        x: valor de numeros que sera sorteado.

    Returns:
         list: Lista contendo os números sorteados.
    """
    numeros = []
    print(f"Sorteando {x} valores da lista: ",end=' ')

    while len(numeros) < x:
        n = randint(0,9)
        if n not in numeros:
            numeros.append(n)
            print(f"{n}",end=' ',flush=True)
            sleep(0.5)

    return numeros


def soma_pares(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print()
    print(f"Somando os valores pares de {lista}, temos {soma}")



numeros = sorteio(5)
soma_pares(numeros)
help(sorteio)
