#Mesmo exemplo, porém, usando o for:
numeros = '1398295'
lista_numeros = []

for num in numeros:
    lista_numeros.append(int(num))
print(lista_numeros)

#Mesmo exemplo, porém, usando o list comprehensions:
numeros = '1398295'
lista_numeros = [int(num) 
                for num in numeros]
print(lista_numeros)

#Mesmo exemplo, porém, usando o map:
map_numeros = map(lambda x: int(x),
                numeros)

print(list(map_numeros))