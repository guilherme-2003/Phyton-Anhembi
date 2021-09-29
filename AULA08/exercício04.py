import re

def mostrar_dstas(texto: str) -> None:
    datas: re.findall(r'[0-3][0-9]/[0-1][0-9]/[1-2][0-9]{3}')
    for data in datas:
        print(data)

texto = input("Digite seu")