import re

texto = "Joao e Maria são nomes próprios."
regex = r'[A-Z][a-z]+'

encontrados = re.findall(regex, texto)
for nome in encontrados:
    print(nome)