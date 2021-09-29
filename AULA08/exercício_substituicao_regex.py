import re

texto = 'O autor (sic) desse texto (sic) escreveu assim mesmo'
# Remove parênteses junto com todos os alfanuméricos e espaços
print(re.sub(r'\([\w\s]+\)', '', texto))
