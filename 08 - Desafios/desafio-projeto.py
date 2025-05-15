# Desafio - Ponto Steak
temperatura = int(input('Digite a temperatura do steak: '))

if temperatura < 48:
    result = 'Ponto - Rare'
elif temperatura in range(48, 53):
    result = 'Ponto - Medium Rare'
elif temperatura in range(54, 59):
    result = 'Ponto - Medium'
elif temperatura in range(60, 64):
    result = 'Ponto - Medium Well'
else:
    result = 'Ponto - Well Done'

print(result)


# Desafio - Calc Pintura
def calc_tinta(altura: int, largura: int) -> int:
    return altura * largura / rendimento


altura = int(input('Digite o tamanho da altura da parede: '))
largura = int(input('Digite o tamanho da largura da parede: '))
rendimento = int(input('Digite o rendimento de tinta: '))

qtd_latas = calc_tinta(altura, largura)
print(f'Voce precisa de {qtd_latas} latas de tintas!')

# Desafio - Filtrando Funcionarios
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sopfia', 'Bruno', 'Melissa']
funcionarios_turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
funcionarios_turno_noite = ['Pedro', 'Sopfia', 'Bruno']
funcionarios_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

funcionarios_carro_noite = set(funcionarios).intersection(funcionarios_turno_noite)
print(funcionarios_carro_noite)

funcionarios_carro_dia = set(funcionarios).intersection(funcionarios_turno_dia)
print(funcionarios_carro_dia)

funcionarios_sem_carro = set(funcionarios).difference(funcionarios_carro)
print(funcionarios_sem_carro)

# Desafio - Calc IMC
altura = float(input('Digite a sua altura em cm: '))
peso = float(input('Digite o seu peso: '))

imc = peso / (altura / 100) ** 2

if imc < 18.5:
    result = 'Status: Magreza'
elif 18.5 < imc < 24.9:
    result = 'Status: Normal'
elif 24.9 < imc < 29.9:
    result = 'Status: Sobrepeso'
elif 29.9 < imc < 39.9:
    result = 'Status: Obesidade'
else:
    result = 'Status: Obesidade Grave'

print(result)
