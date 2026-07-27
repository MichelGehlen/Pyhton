def formatar(msg):
    print("=-"*30)
    print(f'{msg}'.center(60))
    print("=-"*30)

bibloteca = list()
def cadastro():
    livro = dict()
    print()
    livro['Nome'] = str(input("Nome livro: "))
    livro['qtd_pagina'] = int(input("QTD paginas: "))
    livro['Disposicao'] = True
    bibloteca.append(livro)

def listar():
    print()
    print("LISTAGEM".center(60))
    print("=-"*30)
    print(f"{"ID":<10}{"Titulo":<15}{"N.Paginas":<15}{"Status":<15}")
    print("=="*30)
    for k,v in enumerate(bibloteca):
        status = "Disponível" if v['Disposicao'] else "Emprestado"
        print(f"{k:<10}{v['Nome']:<15}{v['qtd_pagina']:<15}{v['Disposicao']:<15}")
        print("-"*30)

def emprestar():
    nome_Emprestimo = str(input("Digite o nome do livro: "))
    
    livro_encontrado = False
    ja_emprestado = False

    for v, k in enumerate(bibloteca):
        if k["Nome"] == nome_Emprestimo:
            livro_encontrado = True
            if k["Disposicao"] == True:
                k["Disposicao"] = False  
                print("\033[0;32mEmprestado com sucesso!!\033[m")
                return  
            else:
                ja_emprestado = True

    if not livro_encontrado:
        print("\033[0;31mErro!!\033[m")
        print("O livro não existe!!")
    elif ja_emprestado:
        print("\033[0;31mErro!!\033[m")
        print("O livro já foi emprestado")   

def devolver():
    nome_devolucao = str(input("Digite o nome do livro: "))

    livro_encontrado = False


    for livro in bibloteca:
        if livro["Nome"] == nome_devolucao:
            livro_encontrado = True
            if livro["Disposicao"] == False:
                livro["Disposicao"] = True
                print("\033[0;32mDevolvido com sucesso!!\033[m")
                return
        if livro["Disposicao"] == True:
            print("\033[0;31mEste livro já estava na biblioteca!\033[m")
            return
    if not livro_encontrado:
        print("\033[0;31mLivro não encontrado no sistema.\033[m")
        return


while True:
    formatar('BIBLIOTECA')
    print()
    print('Opções'.center(30))
    print("-"*30)
    print("1 - Cadastrar livro \n" \
    "2 - Devolver \n"
    "3 - Listar \n" 
    "4 - Estatísticas \n"
    "5 - Emprestar \n"
    "6 - Sair")
    print("-"*30)
    opcao = int(input("Escolha uma opção: "))
    while opcao > 6 or opcao < 1:
        print("\033[0;31mErro!!\033[m")
        opcao = int(input("Escolha uma opção: "))
    match opcao :
        case 1:
            cadastro()
        case 2:
            devolver()  
        case 3:
            listar()
        case 5:
            emprestar()
        case 6:
            break


    
    