# 1 - DETALHES DE UMA STRING

# -> string inline e multiline
msg1 = 'texto inline'
msg2 = '''
texto multiline com quebra de linha
'''

print(msg1)
print(msg2)

# -> indexacao e fatiamento
msg_indexacao = 'test do texto'

print(msg_indexacao[0])
print(msg_indexacao[-3])

print(msg_indexacao[0:4])
print(msg_indexacao[8:13])
print(msg_indexacao[:4])
print(msg_indexacao[-5:])

# 2 - METODOS COMUNS PARA STRING
mensagem_method = "Texto para metodos para comuns"
print(mensagem_method.upper())
print(mensagem_method.lower())
print(mensagem_method.strip())
print(mensagem_method.replace('metodos', 'replace'))
print(mensagem_method.split('para'))

# 2 - UTILIZANDO F-STRING
nome = 'Fernando'
idade = 33

print(f'Meu nome eh {nome}, e tenho atualmente {idade} anos')

# 2 - ADD SEQUENCIAS DE ESCAPE
msg_escape1 = 'aprendendo \npython'
msg_escape2 = 'aprendendo\tpython'
msg_escape3 = 'C:\\diretorio\\'
msg_escape4 = 'aprendendo \'python\''

print(msg_escape1)
print(msg_escape2)
print(msg_escape3)
print(msg_escape4)
