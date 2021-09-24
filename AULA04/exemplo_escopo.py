a = 10

def muda_variavel():
    global a
    a = 7
    print('Variável dentro da função:', a) # 7

print('Antes da mudança:', a) # 10
muda_variavel() # 7
print('Depois da mudança:', a)