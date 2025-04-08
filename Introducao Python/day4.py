# 1 - FUNCAO INPUT()
input_valor = input('digite alguma coisa: ')
print(f'foi digitado: {input_valor}')

# 2 - CRIANDO SEQUENCIA DE INPUTS
nome_test = input('digite seu nome: ')
sobrenome_test = input('digite seu sobrenome: ')

print(f'Seja bem-vindo {nome_test} - {sobrenome_test}')

# 3 - CONVERT STRING PARA INTEGER
idade_test = int(input('digite sua idade: '))

print(f'Sua idade informada: {idade_test}')
print(type(idade_test))

# 4 - PROGRAMA COM INPUT
valor_produto = float(input('digite o valor do produto: '))
resultado_bonus = valor_produto * 1.10

print(f'valor do produto com bonus: {resultado_bonus:.2f}')

# 5 - MULTIPLAS ENTRADAS NA MESMA LINHA DE INPUT()
dados = input('digite seu nome e idade: ').split()
print(f'seu nome eh {dados[0].upper()} com a idade {dados[1]}')
