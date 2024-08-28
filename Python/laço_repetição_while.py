notas = []

contador = 1

while contador <=5:
    codigo_aluno = input("Rm: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    contador = contador + 1
    print("quantidade de notas", len(notas))