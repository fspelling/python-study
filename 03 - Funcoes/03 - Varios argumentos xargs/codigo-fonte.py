# Function com MULTI parametros xargs (*)
def somar_numeros(*numeros):
    resultado = 0

    for num in numeros:
        resultado += num

    print(resultado)


somar_numeros(10, 20, 30)


# Function com MULTI parametros kwargs (**)
def mostar_info_carro(**carro):
    for carroKey, carroValue in carro.items():
        print(f'{carroKey} = {carroValue}')


mostar_info_carro(marca='jeep', cor='azul', motor=2.0)
