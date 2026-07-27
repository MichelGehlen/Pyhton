from datetime import date
ano = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano
if idade ==18:
    print("é hora de se alistar")
elif idade > 18:
    print("já passou o tempo do alistamento")
else:
    print("ainda vai precisar se alistar")