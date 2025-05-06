# Trabalhando com listas auxilares
frutas = ['banana', 'acai', 'morango']
frutas_result = []

for fruta in frutas:
    if 'b' in fruta:
        frutas_result.append(fruta)

print(frutas_result)

# Trabalhando list comprehension
frutas = ['banana', 'acai', 'morango']
frutas_result = [fruta for fruta in frutas if 'b' in fruta]

print(frutas_result)

# Generator Expression
frutas = ['banana', 'acai', 'morango']
frutas_result = (fruta for fruta in frutas if 'b' in fruta)

print(frutas_result)
print(list(frutas_result))
