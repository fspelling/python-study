# 1 - DESAFIO DESCONTO
valor_compra = float(input('informe o valor da compra R$: '))
desconto = 0.05

if valor_compra > 100:
    desconto = 0.10
elif valor_compra > 200:
    desconto = 0.20

valor_final = valor_compra - (valor_compra * desconto)

print(f'Valor final da compra: R$ {valor_final:.2f}')

# 2 - DESAFIO LOGIN
username_admin = 'admin'
password_admin = '123'

username = input('informe seu username: ')
password = input('informe seu password: ')

if username == username_admin and password == password_admin:
    msg = 'Login OK'
else:
    msg = 'Usuario ou senha incorretos'

print(msg)
