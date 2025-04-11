# FOR PARA NUMEROS
for numero in range(5):
    print(numero)

# FOR PARA STRING
palavra = 'Google'
for letra in palavra:
    print(f'\'{letra}\' esta na palavra: \'{palavra}\'')

# FOR COM IF ELSE
compra_validacao = False

for tentativa in range(3):
    if compra_validacao:
        print('a compra de R$ 10,00 foi realizado com sucesso.')
        break
else:
    print('falha na compra, tente novamente...')

# NESTED LOOPS (Loop Outer e Loop Inner)
for numero1 in range(5):
    print(f'LOOP 1 - {numero1}')

    for numero2 in range(5):
        print(f'LOOP 2 - {numero2}')

# Desafio - Separando string com ' '
palavra = 'Google'
for letra in palavra:
    print(letra, end=' ')
