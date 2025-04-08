# 1 - UTILIZANDO O IF
idade_if = 33

if idade_if >= 18:
    print('eh maior de idade!')

# 2 - UTILIZANDO O IF ELSE
idade_if_else = 33

if idade_if_else >= 18:
    result = 'eh maior de idade!'
else:
    result = 'eh menor de idade!'

print(result)

# 2 - UTILIZANDO O IF ELIF ELSE
idade_if_elif = 33

if idade_if_elif < 18:
    result = 'crianca'
elif 18 <= idade_if_elif <= 60:
    result = 'adulto'
else:
    result = 'idoso'

print(result)
