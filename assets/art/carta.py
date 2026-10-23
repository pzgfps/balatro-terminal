from dataclasses import dataclass
from enum import Enum

# a carta devera ser criada como um objeto, porque ela precisa armazenar o valor de naipe e rank, e
# nada mais além disso.

class Naipe(Enum):  # Criacao de um novo tipo de variavel Naipe (enum)
    COPAS   = "♥"
    OUROS   = "♦"
    PAUS    = "♣"
    ESPADAS = "♠"

class Rank(Enum):   # # Criacao de um novo tipo de variavel Rank (enum)
    
    AS = ("A", 11)  # o As vai ter o ícone de A e o valor de pontos 11
    DOIS = ("2", 2) # o dois vai ter o ícone e valor de 2
    TRES = ("3", 3) # o tres vai ter o ícone e valor de 3
    QUATRO = ("4", 4)   # o quatro vai ter o ícone e valor de 4
    CINCO = ("5", 5)    # o cinco vai ter o ícone e valor de 5
    SEIS = ("6", 6)     # o seis vai ter o ícone e valor de 6
    SETE = ("7", 7)     # deu pra entender né
    OITO = ("8", 8)
    NOVE = ("9", 9)
    DEZ = ("10", 10)
    VALETE = ("J", 10)
    DAMA = ("Q", 10)
    REI = ("K", 10)

def __init__(self, simbolo, pontos): # essa funcao pega a tupla de rank e desempacota,
    self.simbolo = simbolo           # sendo possível "usar" cada atributo separadamente sem ser através
    self.pontos = pontos             # de indices, tornando mais legivel e menos fragil

@dataclass(frozen=True)  # isso faz com que o objeto carta tenha valores imutaveis
class Carta:    # o class junto com o dataclass cria o objeto carta
    naipe: Naipe    # atributo do objeto carta (Naipe é um tipo de variavel Naipe)
    rank: Rank      # atributo do objeto carta (Rank é um tipo de variavel Rank)

    @property
    def pontos(self):
        """Pontos base da carta (Ás = 11 por padrão)."""
        return self.rank.pontos

    @property
    def rotulo(self):
        """Ex: 'A♠', '10♥', 'K♦'."""
        return f"{self.rank.simbolo}{self.naipe.value}"

    def __str__(self):
        return self.rotulo