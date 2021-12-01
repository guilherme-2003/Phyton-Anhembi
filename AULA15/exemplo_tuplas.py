dias = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')
n_dias_semana = len(dias)
print('A semana sem fins de semana tem', n_dias_semana)

for dia in dias:
    if dia in 'segunda,quarta,sexta':
        print(f'{dia} passa o lixeiro!')