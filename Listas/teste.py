num = [2, 5, 9, 1]
num[2] = 3
num.append(7) #adiciona valores a lista
num.sort(reverse=True) # ordena a lista, com o reverse ordena do maior pro menor
num.insert(2, 2) # adiciona o valor na posição 2 o valor 0 
#num.pop(2)
num.remove(2) #remove apenas o primerio indice que contem o  numero 2
print(num)
print(f'Essa lista tem {len(num)} elementos') #len retorna quantos elementos tem