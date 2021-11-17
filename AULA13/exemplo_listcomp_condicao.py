todos_numeros = [2, 1, 5, 10, 9, 11, 14, 18, 19, 32, 21]

# O if é colocado em outra linha por ser visualmente mais agradável
lista_pares = [numero for numero in todos_numeros
               if numero % 2 == 0]

# map(funcao, filter(condicao, lista)) -> caso quisesse utilizar map e filter em conjunto

print(lista_pares)