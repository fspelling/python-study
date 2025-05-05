# Criando Sets
lista1 = set([10, 20, 20, 30, 40])
lista2 = set([20, 60, 70])

print(lista1 | lista2)
print(lista1 & lista2)
print(lista1 - lista2)
print(lista1 ^ lista2)

# Funcoes do Set
lista = set([10, 20, 20, 30, 40])

lista.add(50)
print(lista)

lista.update([50, 60, 70, 80])
print(lista)

lista.remove(50)
print(lista)

lista.discard(40)
print(lista)
