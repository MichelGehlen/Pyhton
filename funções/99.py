from time import sleep

def maior(* x):
    print("-="*30)
    print("Analisando os valores...")
    if len(x) == 0:
        print("Foram passados 0 valores")
        print("O maior valor foi 0")
        return
    maior_valor = 0
    cont = 0
    for c in x:
        print(f'{c}',end=' ',flush=True)
        sleep(0.5)
        if cont == 0:
            maior_valor = c
        else:
            if c > maior_valor:
                maior_valor = c
        cont +=1
    print(f"Foram passados {cont} valores")
    print(f"O maior valor foi {maior_valor}")
    print("-="*30)

maior(2,9,4,5,7,1)
maior()
