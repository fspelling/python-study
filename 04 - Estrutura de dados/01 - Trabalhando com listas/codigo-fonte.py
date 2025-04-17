# Criando uma varial do tipo List
lista = [1, 10, 30]
print(type(lista))
print(lista)

# Acessando elementos da lista
lista2 = [1, 10, 30]
print(lista2[0])
print(lista2[-1])

# Funcoes de uma lista
lista3 = [1, 10, 30]

lista3.append(40)
print(lista3)

lista3.remove(40)
print(lista3)

# Duplicando e Concatenando listas
lista_dup = [1, 2, 3]
lista_dup_resultado = lista_dup * 2

print(lista_dup_resultado)

lista_concat_numeros = [1, 2, 3, 3]
lista_concat_letras = ['a', 'b', 'c']
lista_concat_resultado = [*lista_concat_numeros, *lista_concat_letras]

print(lista_concat_resultado)

lista_concat_numeros.extend(lista_concat_letras)
print(lista_concat_numeros)

# Extraindo variáveis em lista
a, b, c = [10, 20, 30]

print(a)
print(b)
print(c)

primeiro, segundo, *outros = [10, 20, 30, 40, 50, 60]

print(primeiro)
print(segundo)
print(*outros)

firt, *meio, last = [10, 20, 30, 40, 50, 60]

print(firt)
print(meio)
print(last)

# Validando itens em uma lista
itens_valid = [1, 2, 3]
item_busca = 1

if item_busca in itens_valid:
    print('item encontrado')
else:
    print('item nao encontrado')

# Mergeando 2 listas com zip
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c', 'd', 'e']

lista_zip = list(zip(lista1, lista2))
print(lista_zip)

# Criando lista a partir de um INPUT()
produtos = input('Digite TODOS seus produtos: ').split(',')
produtos = [prod.strip() for prod in produtos]

print(produtos)
