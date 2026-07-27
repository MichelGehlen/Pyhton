def leiaint(msg):
    valor = 0
    while True:
        n = (input(msg))
        try:
            valor = int(n)
        except (ValueError, TypeError):
            print("\033[0;31mErro!!\033[m")
            continue
        else:
            break
    return valor

def leiafloat(msg):
    valor = 0
    while True:
        x = input(msg)
        try:
            valor = float(x)
        except (ValueError, TypeError):
            print("\033[0;31mErro!!\033[m")
        else:
            break
    return valor

def leiafloat2(msg):
    while True:
        try:
            a = float(input(msg))
        except (ValueError, TypeError):
            print("\033[0;31mErro!!\033[m")
            continue
        except (KeyboardInterrupt):
            print("entrada interrompida pelo usuario")
            return 0
        else:
            return a




n = leiaint("Digite um numero inteiro: ")
x = leiafloat("Digite um numero real: ")
a = leiafloat2("Digite um numero real: ")
print(f"Você digitou o numero {n} ")
print(f"Você digitou o numero {x}")
print(a)