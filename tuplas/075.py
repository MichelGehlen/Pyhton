cont_9 = 0
pos_3 = 0
n = ( int(input("Digite um numero: ")), 
     int(input("Digite um numero: ")), 
     int(input("Digite um numero: ")))
print(f'Você digitou os valores {n}')
for c in range(0, len(n)):
    if n[c] == 9:
        cont_9 +=1 
    if n[c] == 3:
        pos_3 = c+1
print(f'O numero 9 aparece {cont_9}')
print(f"O valor 3 aparece na {pos_3} posição")
print(f"O valores pares são ", end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')