def quebrar_por_delimitadores(conteudo:str,delimitador="$") -> None:
    inicio = 0
    fim = 0

    while fim < len(conteudo):
        # Um for para cada palavra
        while fim < len(conteudo) and conteudo[fim] != '$':
            fim += 1
        
        print(conteudo[inicio : fim])
        fim += 1
        inicio = fim
        
quebrar_por_delimitadores("minha$string$legal")