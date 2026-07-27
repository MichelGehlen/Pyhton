alunos = dict()
notas = list()
alunos['nome'] = str(input("Digite o nome do aluno: "))
tot = int(input("Digite a quantidade de notas: "))
for c in range(1,tot + 1):
    notas.append(int(input(f"Digite a {c}ª nota: ")))
alunos['nota'] = notas[:]
alunos['media'] = sum(notas) / len(notas)
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado' 

for k,v in alunos.items():
    print(f'{k}:{v}')