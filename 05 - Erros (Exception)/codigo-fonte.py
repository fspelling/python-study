# Try e Excepct
try:
    valor = int(input('Digite o valor do produto: '))
    print('O valor foi processado com sucesso...')
except ValueError:
    print('Digite um valor correto!')

# Try e Excepct com Else e Finally
try:
    valor = int(input('Digite o valor do produto: '))
    print('O valor foi processado com sucesso...')
except ValueError:
    print('Erro... Digite um valor correto!')
else:
    print('Codigo esta OK!')
finally:
    print('Codigo que precisa executar com sucesso ou mesmo com erro!')
