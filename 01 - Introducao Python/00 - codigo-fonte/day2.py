import math

# 1 - realizando calculo com numeros
num1 = 10
num2 = 20
resultado = num1 + num2
print(resultado)

# 2 - operador de atribuicao aumentada
numero = 10
numero += 2
print(numero)

numero *= 2
print(numero)

# 3 - funcoes basicas para numeros

# -> round() - funcao que arrendonda o valor para cima ou para baixo
print(round(3.545))

# -> round(num, casas) - funcao que arrendonda o valor para cima ou para baixo,
# porem com casas decimais definidas nesse arrendondamento
print(round(3.546, 1))
print(round(3.546, 2))

# -> pow() - funcao que realiza a potencia de um numero
print(pow(2, 3))

# -> max() - funcao que retorna o valor maximo de uma lista
print(max(2, 3, 1, 7, 4))

# -> min() - funcao que retorna o valor minimo de uma lista
print(max(2, 3, 1, 7, 4))

# -> sum() - funcao que soma os valores  de uma lista
print(sum([1, 3, 6]))

# 4 - modulo math
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pow(2, 3))
