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