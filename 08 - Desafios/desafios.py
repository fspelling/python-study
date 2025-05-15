# Desafio - Contador de lista
frutas = ['maca', 'uva', 'morango', 'maca', 'maca', 'banana']

qtde_maca = len([fruta for fruta in frutas if fruta == 'maca'])
qtde_maca_simple = frutas.count('maca')

print(f'temos {qtde_maca} macas.')
print(f'temos {qtde_maca_simple} macas.')

# Desafio - Pesquisa de pais e capital
lista_pais_capital = {
    'Brasil': 'Brasilia',
    'Estados Unidos': 'New York',
    'Argentina': 'Buenos Aires'
}

pais = input('Informe o pais desejado: ')

if pais in lista_pais_capital:
    print(f'A capital de {pais} eh {lista_pais_capital.get(pais)}.')
else:
    print('Nao foi encontrado o pais informado!')

# Desafio - Encontrando um item no while
fruta_find = ''

while fruta_find.lower().strip() != 'banana':
    fruta_find = input('Digite uma fruta: ')

print('banana foi encontrada!')

# Desafio - Comparacao Sets
nomes1 = set(['Fernando', 'Bruno', 'Rafael'])
nomes2 = set(['Fernando', 'Arthur', 'James'])

print(f'Colecao de intersection: {nomes1.intersection(nomes2)}')


# Desafio - Funcao que realiza soma
def somar(*numeros: int) -> int:
    return sum(numeros)


numero1 = int(input('Informe o numero 1 desejado: '))
numero2 = int(input('Informe o numero 2 desejado: '))

print(f'A soma eh: {somar(numero1, numero2)}')

# Desafio - funcao com parametro opcional
def potencia(num_base, num_expo = 2):
    return num_base ** num_expo


num_base = int(input('Informe o numero base: '))
num_expo = input('Informe o numero expo: ')
retorno_potencia = potencia(num_base, int(num_expo)) if num_expo else potencia(num_base)

print(f'o numero expo de {num_base} eh: {retorno_potencia}')

# Desafio - funcao recursiva
def fatorial(num):
    if (num <= 1):
        return 1
    else:
        return num * fatorial(num - 1)


num = int(input('Informe o numero da potencia: '))
result = fatorial(4)

print(f'O fatorial eh: {result}')

# Desafio - Lambda com if else
num = int(input('Informe o numero: '))
imprimir_par_impar = lambda num: 'PAR' if num % 2 == 0 else 'IMPAR'

print(f'O numero eh: {imprimir_par_impar(num)}')

# Desafio - Lambda com for loop
quadrado_list = lambda lista: [n ** 2 for n in lista]
result = quadrado_list([1, 2, 4])

print(result)
