bibloteca = []
while True:
    livro = {}
    livro['Título'] = str(input("Título: "))
    livro['Autor'] = str(input("Autor: "))
    livro['Paginas'] = int(input("Paginas: "))
    bibloteca.append(livro.copy())
    r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while r not in 'SN':
        print("ERRO! reponda com S/N ")
        r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if r == 'N':
        break

soma = 0
for c in bibloteca:
    soma += c['Paginas']
media = soma / len(bibloteca)

print("-="*30)
print(f"BIBLIOTECA".center(60))
print("-="*30)
for livro in bibloteca:
    for k,v in livro.items():
        print(f'{k}: {v}')
    print("-"*30)

print(f"A quantidade de livros na bibloteca é: {len(bibloteca)}")
print(f"A média de paginas dos livros na bibloteca é: {media:.1f}")
print(f"Os livros acima da média de paginas são: ")
for livro in bibloteca:
    if livro['Paginas'] >= media:
        print(' ')
        print(f"Título:{livro['Título']} \nPaginas:{livro['Paginas']}")