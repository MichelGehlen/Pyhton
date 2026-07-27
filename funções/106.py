c = {
    'limpa':    '\033[m',
    'branco':   '\033[30m',
    'vermelho': '\033[31m',
    'verde':    '\033[32m',
    'amarelo':  '\033[33m',
    'azul':     '\033[34m',
    'roxo':     '\033[35m',
    'ciano':    '\033[36m',
    'cinza':    '\033[37m',
    'f_branco':  '\033[40m',
    'f_vermelho':'\033[41m',
    'f_verde':   '\033[42m',
    'f_amarelo': '\033[43m',
    'f_azul':    '\033[44m',
}

def ajuda(com):
    titulo(f"Acessando o manual do comando \'{com}\'","f_amarelo")
    print(c['f_azul'], end="")
    help(com)

def titulo(msg,cor=0):
    tam = len(msg)
    print(c[cor],end='')
    print("~" * tam)
    print(f'{msg}')
    print("~" * tam)
    print(c['limpa'])

#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP','roxo')
    comando = str(input("Função ou Bibloteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO",'vermelho')
