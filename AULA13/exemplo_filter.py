numeros = [2, 5, 7, 9, 10, 8]
impares = filter(lambda x: x % 2 != 0, numeros)

for num in impares:
    print(num)