maiores = 0
menores = 0
from datetime import date
for c in range (1,7+1):
    ano = int(input(f"Em que ano a {c} pessoa nasceu? "))
    idade = date.today(). year - ano
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print("Ao todo tivemos {} pessoas maiores de idade".format(maiores))
print("E também tivemos {} pessoas menores de idade".format(menores))
 