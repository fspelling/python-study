from array import array

# Trabalhando com Tuples
cores = ('cor a', 'cor b', 'cor c')
print(type(cores))

# Trabalhando com Array
array_texto = array('u', ['a', 'b', 'c'])
array_int = array('i', [1, 2, 3])
array_float = array('f', [1.9999, 2.9999, 3.9999])

print(array_texto.tolist())
print(array_int.tolist())
print(array_float.tolist())
