# Introducao aos dictionarys
alunoDic = {'nome': 'Ana', 'idade': 16, 'cidade': 'SP'}

print(type(alunoDic))
print(alunoDic)

# Atualizando itens dic
alunoDic = {'nome': 'Ana', 'idade': 16, 'cidade': 'SP'}

alunoDic['idade'] = 17
alunoDic.update({'idade': 19})

print(alunoDic['nome'])

print(alunoDic.get('nome'))
print(alunoDic.get('nome2', 'chave nao encontrada'))

# Looping no Dic
alunoDic = {'nome': 'Ana', 'idade': 16, 'cidade': 'SP'}

for aluno in alunoDic.keys():
    print(aluno)

for aluno in alunoDic.values():
    print(aluno)

for key, value in alunoDic.items():
    print(f'{key} - {value}')
