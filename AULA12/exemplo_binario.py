arquivo=open('aula12_handout.pdf','rb')
# rb significa leitura em forma de bytes
byte = arquivo.read(1)
while byte:
    print(byte)
    byte = arquivo.read(1)
arquivo.close()