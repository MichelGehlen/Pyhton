from datetime import date
ano = int(input("Digite o ano em que você nasceu: "))
idade = date.today().year - ano
if idade <=9:
    print("Mirim")
elif 9> idade <=14:
    print("Infantil")
elif 14 < idade >= 19:
    print("junior")
else:
    print("senior")
