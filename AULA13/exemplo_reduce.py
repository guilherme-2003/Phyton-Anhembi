from functools import reduce

lista = [1,3,4,6,2,6,2,6]

print(reduce(lambda a, b: a + b, lista))