# Procurar caracteres alfanuméricos apenas
import re

# String alfanumérica
string_alfa_num = "Isso é um4 str1ng c0m mu1t0s caracteres alfanumér1cos"

ocorrencias = re.findall(r'[a-zA-Z0-9\s]', string_alfa_num)

for ocorren in ocorrencias:
    print(ocorren)

# Pegar sequências de letras
                                    # Maior sequência de letras possível
maior_sequencia_letras = re.findall(r'[a-zA-Z]+[0-9]*\s*', string_alfa_num)

for palavra in maior_sequencia_letras:
    print(palavra)

# Frases que terminam com interrogação
termina_com_interrogacao = "Uma frase. \nOutra frase. \nMais uma frase?"
perguntas = re.findall(r'\n[A-Za-z\s]+\?', termina_com_interrogacao)

for p in perguntas:
    print(p)