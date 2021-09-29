import re

informacoes = "O telefone do usuário é 98127-3909. 4444-4444"

# O search encontra um único resultado que bate com o padrão buscado
resultado = re.search(r"[0-9]+-[0-9]+", informacoes)

# O findall encontra todas as ocorrências do padrão buscado
resultado_findall = re.findall(r"[0-9]+-[0-9]+", informacoes)

if resultado is not None:
    print(resultado.group(0))

print('resultado findall:')
for ocorrencia in resultado_findall:
    print(ocorrencia)