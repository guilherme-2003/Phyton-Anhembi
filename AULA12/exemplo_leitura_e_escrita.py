# Podemos ler do arquivo ou escrever nele nesse modo

arquivo = open('numeros.txt','r+')
arquivo.read()
arquivo.write('Lendo e escrevendo\n')
arquivo.close()