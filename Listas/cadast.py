dados = list()
pessoas = list()

while True:
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))

    dados.append(nome)
    dados.append(idade)

    nome_duplicado = False
    if len(pessoas) > 0:
        for i in range(len(pessoas)):
            if nome == pessoas[i][0]:
                nome_duplicado = True
                break

    if nome_duplicado:
        print('Nome duplicado não irei adicionar!! ')
    else:
        print('Pessoa adicionada com sucesso!!')
        pessoas.append(dados[:])
        dados.clear()

    resp = str(input('Deseja adicionar outra pessoa? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break


print(f'Você digitou {len(pessoas)} dados de pessoas ')
while True:
    print('-='*30)
    print('DADOS'.center(60))
    print('-='*30)
    escolha = int(input('(1) Busca por nome  \n' \
                    '(2) Dados           \n' \
                    '(3) Sair            \n'))
    if escolha == 3:
        break

    match escolha:
        case 1:
            print('-='*30)
            print('BUSCA POR NOME'.center(60))
            nome_busca = str(input("Digite o nome que deseja buscar: "))
            for pessoa in pessoas:
                encontrado = False
                if nome_busca == pessoa[0]:
                    print(pessoa)
                    encontrado == True
                if not encontrado:
                    print('Nome não encontrado!! ')
        case 2:
            print('=-'*30)
            print('CADASTROS'.center(60))
            for i in range(len(pessoas)):
                print(f'{pessoas[i]} \n')
        
            
