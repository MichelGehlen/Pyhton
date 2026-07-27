lista = list()
dados = list()
r = 'S'
cont = 0
while r == 'S':
    nome = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Nota 1: '))
    nota2 = int(input('Nota 2: '))
    lista.append(cont)
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append((nota1 + nota2)/2)
    dados.append(lista[:])
    lista.clear()
    cont +=1
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Responda apenas com [S/N]: ')).strip().upper()[0]
print('-='*30)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":<5}')
print('-'*30)

for i in range(len(dados)):
    print(f'{dados[i][0]:<5}{dados[i][1]:<10}{dados[i][4]:<5}')
print('-'*30)

n = 0
while n != 999:
    n = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if 0 <= n < len(dados):
        print(f'Notas de {dados[n][1]} são {dados[n][2]} e {dados[n][3]}')
    else:
        print('Aluno não encontrado!')
    if n != 999:
        print(f'Notas de {dados[n][1]} são {dados[n][2]} e {dados[n][3]}')
    else:
        print('Obrigado por usar o programa!')
    