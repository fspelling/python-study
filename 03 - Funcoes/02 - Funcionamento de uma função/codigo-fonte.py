# Funcao sem parametros
def funcao_teste():
    print('criando funcao')


def somar():
    resultado = 10 + 20
    print(resultado)


funcao_teste()
somar()


# Funcao com parametros
def somar_dois_numeros(numero1: float, numero2: float):
    resultado = numero1 + numero2
    print(f'{resultado:.2f}')


somar_dois_numeros(10, 20)


# Funcao com parametros DEFAULT
def funcao_default(valor='DEFAULT'):
    print(valor)


funcao_default()


# Funcao com RETURN ANY
def funcao_return_any():
    return 'Tipado Dinamico(ANY)'


print(funcao_return_any())


# Funcao com RETURN TIPADO
def funcao_return_tipo() -> str:
    return 'Tipado'


print(funcao_return_tipo())
