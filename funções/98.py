from time import sleep

def contagem(i,f,p):
    print("=-"*30)
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.2)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f"{cont}",end=' ',flush=True)
            sleep(0.2)
            cont -=p



contagem(1,10,1)
contagem(10,0,2)
print(" ")
print('-='*30)
print("Agora é sua vez de personalizar a contagem! ")
inicio = int(input('inicio: '))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contagem(inicio,fim,passo)
  