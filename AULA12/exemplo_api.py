import requests
import urllib
import json

def devolver_coordenadas(json_enderecos: dict) -> 'tuple[float, float]':
    primeiro_endereco = json_enderecos['features'][0]
    longitude = primeiro_endereco['geometry']['coordinates'][0]
    latitude = primeiro_endereco['geometry']['coordinates'][1]
    # Devolve as coordenadas do endereço em forma de tupla
    return (latitude, longitude)

def ler_token() -> str:
    with open('accesstoken.txt', 'r') as arquivo:
        token_acesso = arquivo.read()
        return token_acesso.strip('\n')

def buscar_json(endereco: str, token_acesso: str) -> dict:
    url_api = f'''
        https://api.mapbox.com/geocoding/v5/mapbox.places/
        {endereco}.json?access_token={token_acesso}'''
    conteudo = requests.get(url_api).text
    # Json contendo os endereços que batem com a busca
    json_enderecos = json.loads(conteudo)
    return json_enderecos

token = ler_token()
print(buscar_json('Brazil', token))
endereco = "Rua Casa do Ator, 275, Vila Olímpia, São Paulo"
# Converte o endereço para o formato de url
endereco_url = urllib.parse.quote_plus(endereco)
token_acesso = ler_token()
json_enderecos = buscar_json(endereco_url, token_acesso)
print(devolver_coordenadas(json_enderecos))