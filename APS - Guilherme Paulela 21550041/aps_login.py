from os import write
import re

regex = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[$@#])[0-9a-zA-Z$@#]{8,}$")
senha = 'senha_errada'

nome_do_usuario = input("Cadastre um nome de usuário: ")

while not regex.match(senha):
    print("\nDigite uma senha válida!\nSua senha deve seguir os padrões:\n- No mínimo 8 caracteres\n- Pelo menos uma letra MAIÚSCULA\n- Pelo menos uma letra MINÚSCULA\n- Pelo menos um NÚMERO\n- Pelo menos um CARACTERE ESPECIAL ($#@)")
    senha = input("Cadastre uma senha: ")

print("\nUsuário e senha salvos!\n")

with open('login.txt', 'w') as arquivo:
    arquivo.write(f"Username: {nome_do_usuario}\nSenha: {senha}")