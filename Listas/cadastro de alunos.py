dados = list()
alunos = list()
aprovados = list()
reprovados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Nota: ')))
    if dados[1] > 7:
        aprovados.append(dados[:])
    else:
        reprovados.append(dados[:])
    alunos.append(dados[:])
    dados.clear()
    r = str(input("Deseja continuar: [S/N] ")).strip().upper()[0]
    if r == 'N':
        break

print("-=" * 30)
print(f'Quantidade de alunos cadastrados: {len(alunos)}')

print("-=" * 30)
print('ALUNOS APROVADOS')

for aluno in aprovados:
    print(f'{aluno[0]} - Nota {aluno[1]}')

print("-=" * 30)
print('ALUNOS REPROVADOS')

for aluno in reprovados:
    print(f'{aluno[0]} - Nota {aluno[1]}')