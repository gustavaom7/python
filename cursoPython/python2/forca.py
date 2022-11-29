import random

def carrega_palavra_secreta():
    # open file
    arquivo = open("lista_frutas", "r")
    banco_palavras = []

    for linha in arquivo:
        linha = linha.strip()
        # all words are being stored in banco_palavras
        banco_palavras.append(linha)

    # close file
    arquivo.close()

    # get a random index
    numero = random.randrange(0, len(banco_palavras))

    # get a random word
    palavra_secreta = banco_palavras[numero].lower()
    return palavra_secreta

def inicializa_letras_acertadas(palavra_secreta):
   return ["_" for letra in palavra_secreta]

def jogar():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):
        chute = input("\n Qual a letra meu parceiro? \n")
        chute = chute.casefold().rstrip().lstrip() #casefold -> not case sensitive; lstrip/rstrip -> remove spaces in the begging/end of the string

        index = 0
        aux = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_acertadas[index] = chute
                aux+=1
            index=index+1
        if(aux == 0):
            tentativas+=1
            enforcou = tentativas == 6 #numero maximo de tentativa\
            if enforcou == True:
                print("Errou tudo cabra da peste! Tenta dinovo!")
            else:
                print("Tenta ota mizeravi! Num tem a letra {} naum".format(chute))
        else:
            print("\nAcertou mizeravi! Temos a letra {}:\n".format(chute))
            print(letras_acertadas)
            if("_" not in letras_acertadas):
                acertou = True
                print("Parabens mizeravi! Acertô tudin")

def mensagem_abertura():
    print("\n*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")


if(__name__ == "__main__"):
    jogar()
