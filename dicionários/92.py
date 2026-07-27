from datetime import datetime
pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))
nasc = int(input("Ano de nascimento: "))
pessoa['idade'] = datetime.now().year - nasc
pessoa['Carteira'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['Carteira'] != 0:
    pessoa['Ano_contrac'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = int(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['Ano_contrac'] + 35) - datetime.now().year)

print('-='*30)
for k,v in pessoa.items():
        print(f'{k} tem o valor {v}')


