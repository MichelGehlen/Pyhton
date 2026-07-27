def somar(a=0,b=0,c=0):
    """Somar
    Soma até três números.

    Args:
         a (int): Primeiro número. Padrão é 0.
        b (int): Segundo número. Padrão é 0.
        c (int): Terceiro número. Padrão é 0.

    Returns:
       int: Resultado da soma dos números.
    """
    s=a + b + c
    return s


r1 = somar(4,6,7)
r2 = somar(4,2,3)
r3 = somar(9,6)

print(f"Os resultados foram {r1},{r2},{r3}")