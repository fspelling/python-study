# Utilizando função lambda
soma = lambda num1, num2: num1 + num2
print(soma(1, 2))


# Função lambda dentro de outra função
def somar(num1: int, num2: int) -> int:
    inc = lambda num: num + 10
    return inc(num1) + num2


valor = somar(10, 20)
print(valor)


# funcao map com lista
def multi_par(num: int) -> int:
    return num * 2


lista = [1, 2, 3, 4]
lista_map = map(multi_par, lista)

print(list(lista_map))

# map com funcao lambda
lista = [1, 2, 3, 4]
print(list(map(lambda num: num * 2, lista)))

# filter com funcao lambda
lista = [1, 2, 3, 4]
print(list(filter(lambda num: num <= 2, lista)))
