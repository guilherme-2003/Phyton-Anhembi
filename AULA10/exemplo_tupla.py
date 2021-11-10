tupla = ('a', 'b', 'c')
print(tupla[0]) # Mostra 'a'
print(tupla[:2]) # Mostra ('a', 'b')
print(tupla * 2) # Mostra ('a', 'b', 'c', 'a', 'b', 'c')
print(tupla[-1]) # Mostra 'c'

tuplavazia = ()

tupla = (1, 2, 'a', 'b') # Tuplas admitem mais de um tipo
for elemento in tupla:
    print(elemento)
