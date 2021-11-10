""" Faça um programa que converta uma lista de temperaturas de Fahrenheit para Celsius. – Em seu programa o usuário deverá inserir uma sequência de valores que
representam a temperatura em graus Fahrenheit – Seu programa deve receber esses valores e armazenar em uma lista até que o valor inserido pelo usuário seja um valor 
em branco (uma string vazia). – Converta todos os valores presentar na lista para graus Celsius e imprima na tela em uma formatação amigável ao usuário. """

temperaturas = []
temp = 'vazio'

while temp != '':
    temp = input("Digite uma temperatura qualquer: ")
    if temp != '':
        tempFahrenheit = float(temp)
        tempCelsius = (tempFahrenheit - 32) * 5 / 9
        # Adiciona as temperaturas a uma tupla
        temperaturas.append(
            (tempFahrenheit, tempCelsius))

for tuplaTemperatura in temperaturas:
    fahr = tuplaTemperatura[0]
    celsius = tuplaTemperatura[1]
    
    print(f'{fahr:.1f} °F - {celsius:.1f} °C')