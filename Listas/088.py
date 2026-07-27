from random import randint
lista = list()
jogos = list()
print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)
q = int(input('Quantos jogos você quer que eu sortei? '))
i = 1
print('-='*3,f'SORTEANDO {q} JOGOS','-='*3)
while i <=q:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    i += 1
for c,l in enumerate(jogos):
    print(f'Jogo {c+1}: {l}')
    