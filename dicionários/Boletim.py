alunos = []
while True:
    aluno = {}
    aluno['Nome'] = str(input("Nome: "))
    aluno['Nota 1'] = int(input("Nota1: "))
    aluno['Nota 2'] = int(input("Nota2: "))
    aluno['Nota 3'] = int(input("Nota3: "))
    aluno['Media'] = (aluno['Nota 1'] + aluno['Nota 2'] + aluno['Nota 3']) / 3
    alunos.append(aluno.copy())
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0] 
    if resp == 'N':
        break
print('-='*30)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":<5}')
for c,i in enumerate(alunos):
    print(f'{c:<5}{i["Nome"]:<10}{i["Media"]:<5.1f}')
print('-='*30)
print(f"{'CONSULTA NOTAS':^60}")
print('-='*30)
busca = 0
while busca!= 999:
    busca = int(input('Digite o numero do aluno (999 encerra): '))
    if 0 <= busca <len(alunos):
        print(f'Nome:{alunos[busca]["Nome"]}\nNotas:{alunos[busca]["Nota 1"]},{alunos[busca]["Nota 2"]},{alunos[busca]["Nota 3"]}')
    elif busca !=999:
        print("Aluno não encontrado")
    

    