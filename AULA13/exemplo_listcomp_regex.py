import re

def remover_pontuacao(frase: str) -> str:
    return re.sub(r'[,!\?]', '', frase)

frases_com_pontuacao = ['Olá, bom dia para você!',
                        'Alo, quem fala?']

frases_sem_pontuacao = [remover_pontuacao(frase)
                        for frase in frases_com_pontuacao]

print(frases_sem_pontuacao) 