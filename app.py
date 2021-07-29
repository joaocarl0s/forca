#Importando o arquivo 'palavras' e a função 'random'.
from palavras import palavras
import random

#Selecionando palavras.
def selecionarPalavra():
    palavra = random.choice(palavras)
    return palavra.upper