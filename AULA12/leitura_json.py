import json
import os #ele identifica o sistema operacional e usa os parâmetros com o separador corredo

caminho_completo = os.path.join('jsons', 'nomes.json')

with open(caminho_completo, 'r') as arquivo:
    conteudo = json.load(arquivo)
    print(conteudo)