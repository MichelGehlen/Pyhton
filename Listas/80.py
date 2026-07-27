valores = []
x = 0
while x < 5:
    x = x + 1
    numero = int(input('Digite um valor: '))
    valores.insert(numero, numero)
    
print(f'{valores}')
