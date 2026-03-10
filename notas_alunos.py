

quantidade = int(input("Quantidade de alunos:"))

nota = [0.0 for x in range(quantidade)]
nota2 = [0.0 for x in range(quantidade)]
aluno = ["" for x in range(quantidade)]


for i in range(0, quantidade):
    aluno[i] = str(input("Aluno:"))
    nota[i] = float(input("Nota 1: "))
    nota2[i] = float(input("Nota 2: "))

aprovado = 0
reprovado = 0
for i in range(0, quantidade):
    media = (nota[i] + nota2[i]) / 2

    if media >= 6:
        situacao = "Aprovado"
        aprovado = aprovado + 1

    else:
        situacao = "Reprovado"
        reprovado = reprovado + 1

    print()
    print(aluno[i])
    print(f"Nota 1: {nota[i]}")
    print(f"Nota 2: {nota2[i]}")
    print(f"Média: {media}")
    print(situacao)

print()
contador = 0
maior = nota[0]
for i in range(0, quantidade):
    if (nota[i] + nota2[i]) / 2 > (nota[contador] + nota2[contador]) / 2:
        contador = i

    if nota[i] > maior:
        maior = nota[i]

    if nota2[i] > maior:
        maior = nota2[i]


print(f"Melhor aluno(a): {aluno[contador]}")
print(f"Maior nota: {maior}")
print()
print(f"Aprovados: {aprovado}")
print(f"Reprovados: {reprovado}")








