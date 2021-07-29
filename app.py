#Importando o arquivo 'palavras' e a função 'random'.
from palavras import palavras
import random

#Selecionando palavras.
def selecionarPalavra():
    palavra = random.choice(palavras)
    return palavra.upper()

#Iniciando jogo.
def jogar(palavra):
    #Definindo variáveis
    palavra_incompleta = "_" * len(palavra)
    advinhou = False
    letras_utilizadas = []
    palavras_utilizadas = []
    tentativas = 6

    print(palavra)
    print(palavra_incompleta)

    #Boas vindas
    print("Começando Jogo.")
    print(exibirForca(tentativas))
    print("Esta é a palavra: ", palavra_incompleta)

    #While o usuário não adivinhar e houver tentativas.

    while not advinhou and tentativas > 0:
        palpite = input("Digite uma palavra ou letra para continuar: ").upper()
        print(palpite)

        #Tentativa de letra única.
        #Verificando se a tentativa é uma letra única.

        if len(palpite) == 1 and palpite.isalpha():
            #Validando se a letra ja foi usada.
            if palpite in letras_utilizadas:
                print("Você ja utilizou essa letra antes: ", palpite)

            #Validando se ela não esta na palavra.
            elif palpite not in palavra:
                print("A letra",palpite,"não está na palavra")
                tentativas -= 1
                letras_utilizadas.append(palpite)
            #Quando a letra está na palavra?
            else:
                print("Você acertou! A letra", palpite ,"esta na palavra")
                letras_utilizadas.append(palpite)
                #Transformar a palavra em lista.
                palavra_lista = list(palavra_incompleta)
                #Valida onde pode substitutuir o underline baseado na letra que foi passada.
                indices = [i for i, letra in enumerate(palavra) if letra == palpite]
                for indice in indices:
                    palavra_lista[indice] = palpite
                palavra_incompleta = "".join(palavra_lista)

                if "_" not in palavra_incompleta:
                    advinhou = True

        #Tentativa inválida
        else:
            print("Palpite inválido, try again!")
        
        #Exibir o status do jogo.
        print(exibirForca(tentativas))
        print(palavra_incompleta)

    #Finaliza o jogo se o usuario venceu ou acabaram as tentativas
    if advinhou:
        print("Parabéns! Você adivinhou")
    else:
        print("Acabaram as chances.. A palavra era", palavra)
#Status do jogo
def exibirForca(tentativas):
    estagios = [# Fim de jogo
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / \\
                  -
              """,
              # Falta 1 tentativa
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |     / 
                  -
              """,
              # Faltam 2 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|/
                  |      |
                  |      
                  -
              """,
              # Faltam 3 tentativas
              """
                  --------
                  |      |
                  |      O
                  |     \\|
                  |      |
                  |     
                  -
              """,
              # Faltam 4 tentativas
              """
                  --------
                  |      |
                  |      O
                  |      |
                  |      |
                  |     
                  -
              """,
              # Faltam 5 tentativas
              """
                  --------
                  |      |
                  |      O
                  |    
                  |      
                  |     
                  -
              """,
              # Estado inicial
              """
                  --------
                  |      |
                  |      
                  |    
                  |      
                  |     
                  -
              """
    ]

    return estagios[tentativas]

#Iniciação do jogo e validação para continuar.
def inicioJogo():
    palavra = selecionarPalavra()
    jogar(palavra)

inicioJogo()