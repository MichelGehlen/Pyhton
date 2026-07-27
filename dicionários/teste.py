pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade': 22}
print(pessoas)
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k,v in pessoas.items():
    print(f'{k} = {v}')