tipos_animais = {'lagarto': 'réptil', 'panda': 'mamífero', 'garoupa': 'peixe'}

if 'lagarto' in tipos_animais:
    print('O dicionário tem a chave lagarto.')
else:
    print('O dicionário não tem a chave lagarto.')

for animal in tipos_animais:
    tipo = tipos_animais[animal]
    print(f'{animal} - {tipo}')

# Mostrará na tela:
# ----------------
# lagarto - réptil
# panda - mamífero
# garoupa - peixe
