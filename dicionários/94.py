pessoas = []
mulheres = []
maiores = []
while True:
    pessoa = {}
    pessoa['Nome'] = str(input("Nome: "))
    pessoa['Sexo'] = str(input("Sexo: [M/F] ")).upper().strip()[0]
    while pessoa['Sexo'] not in "MF":
            print("ERRO!, digite apenas M ou F")
            pessoa['Sexo'] = str(input("Sexo: [M/F] ")).upper().strip()[0]
    if pessoa["Sexo"] == 'F':
          mulheres.append(pessoa["Nome"])
    pessoa["Idade"] = int(input("Idade: "))
    pessoas.append(pessoa.copy())
    resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    while resp not in "SN":
          print('Erro! apenas [S/N] ')
          resp = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if resp == "N":
          break
media = sum(p['Idade'] for p in pessoas) / len(pessoas)
print("-="*30)
print(f"A) Ao todo temos {len(pessoas)} cadastradas.")
print(f"B) A média de idade é de {media:.1f} anos.")
print(f"C) As mulheres cadastradas foram {mulheres}")
print(f"D) Lista das pessoas que estão acima da média: ")
for c in pessoas:
      if c["Idade"] >= media:
            print('')
            for k,v in c.items():
                  print(f'{k} = {v}:',end=' ')
            print()

