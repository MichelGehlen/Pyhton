nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = nota1+nota2/2
if media < 5:
    print("Reprovado")
elif 7 > media >= 5:
    print("Recuperação")
else:
    print("Aprovado")