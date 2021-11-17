""" • Altere o seguinte código que utiliza map e filter para que ele faça a
mesma coisa utilizando listcomps.

import re

emails = ['gustavo.custodio@anhembi.br', 'FULANODETAL@yahoo.com.br.',
          'meuemail.com.br', 'outroemail.com']

def limpar_email(email: str)-> str:
    return email.strip('.').lower()

def validar_email(email: str)-> bool:
    if re.match(r'[\w\.]+@[\w]+.[a-z]+(\.[a-z]+)*', email) is not None:
        return True
    return False

emails_limpos = map(limpar_email, emails)
emails_validos = filter(validar_email, emails_limpos) 

print(list(emails_validos)) """

import re

def limpar_email(email: str)-> str:
    return email.strip('.').lower()

def validar_email(email: str)-> bool:
    if re.match(r'[\w\.]+@[\w]+.[a-z]+(\.[a-z]+)*', email) is not None:
        return True
    return False

emails = ['gustavo.custodio@anhembi.br', 'FULANODETAL@yahoo.com.br.',
          'meuemail.com.br', 'outroemail.com']

emails_validos = [limpar_email(email) 
                  for email in emails
                  if validar_email(email)]

print(emails_validos)