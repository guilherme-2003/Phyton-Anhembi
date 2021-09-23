#tipos de formatação de saída de dados
resultado = 10
#placeholders:
print('Resultado encontrado: %d' %resultado)
# %d para inteiros, %f para decimais e %s para strings

#format:
print('Resultado encontrado: {}' .format(resultado))

#f-strings
print(f'Resultado encontrado: {resultado}')