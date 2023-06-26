"""
Este código gera senhas aleatórias utilizando letras, numeros e caracteres especiais
""""
print("Gerador de senhas")
import random
import string
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.digits + "!@#?" * 3
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
opcao = "s"
while opcao :
    if opcao.lower() == "s" :
        tamanho_senha = int(input("Digite a quantidade de caracteres que deseja: "))
        senha_gerada = gerar_senha(tamanho_senha)
        print("A senha gerada é:", senha_gerada)
        opcao = input("Deseja fazer outra senha? ")
        if opcao.lower() != "s" :
            break
