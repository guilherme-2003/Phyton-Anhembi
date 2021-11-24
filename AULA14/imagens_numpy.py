from PIL import Image
import numpy as np

def pegar_negativo(img: 'np.ndarray'):
    negativo = 255 - img
    Image.fromarray(negativo).save('lena_negativo.jpg')

def salvar_canal_cor(img_copia: 'np.ndarray', cor: str):
    img_copia = img.copy()
    if cor == 'vermelho':
        img_copia [:,:, (1,2)] = 0
    elif cor == 'verde':
        img_copia [:,:, (0,2)] = 0
    else:
        img_copia [:,:, (0,1)] = 0
    Image.fromarray(img_copia).save(f'lena_{cor}.jpg')

img = np.array(Image.open('lena.jpg'))
pegar_negativo(img)
salvar_canal_cor(img, 'vermelho')
salvar_canal_cor(img, 'verde')
salvar_canal_cor(img, 'azul')
print('Imagem salva com sucesso')