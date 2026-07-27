teste = list()
teste.append('Gustavo')
galera = list()
teste.append(40)
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
