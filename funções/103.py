def ficha(nome="desconhecido", gols=0):
    print(f"O jogador {nome} fez {gols} gols no campeonato. ")


nome = str(input("Nome: "))
gols = int(input("Gols: "))
ficha(nome,gols)