""" • Considere o seguinte código:

frutas = ['laranja', 'morango', 'banana', 'manga']
frutascom_m = []
for fruta in frutas:
    if fruta[0] == 'm':
        frutascom_m.append(fruta)
print(frutascom_m)

• Modifique o código, utilizando list comprehension nos lugares
apropriados. """

frutas = ['laranja', 'morango', 'banana', 'manga']

frutas_com_m = [fruta.upper()
                for fruta in frutas 
                if fruta[0] == 'm']

print(frutas_com_m)