from dataclasses import dataclass
from typing import override                 #Esse import serve apenas para que o @override possa aparecer no programa, mas ele nem funciona direito
import random

@dataclass
class Coringa:
    nome: str
    preco: int

    def efeito():               #Um método que deve ser sobreescrito nas classes dos Coringas
        return

class CoringaJoker(Coringa):            #Esse parenteses é onde fica a classe pai, como se fosse "class CoringaJoker extends Coringa"
    nome = "Joker"
    preco = 4

    @override
    def efeito(self, pontuacao, mult, descarte):
        return mult + 4

class CoringaMisprint(Coringa):
    nome = "Erro de impressão"
    preco = 4

    @override
    def efeito(self, pontuacao, mult, descarte):
        numAleatorio = random.randint(0, 23)
        return mult + numAleatorio

class CoringaDusk(Coringa):
    nome = "Cume Místico"
    preco = 5

    @override
    def efeito(self, pontuacao, mult, descarte):
        if(descarte == 0):
            return mult + 4
        return mult

class CoringaMime(Coringa):
    nome = "Mímico"
    preco = 5

    @override
    def efeito(self, pontuacao, mult, descarte):
        return
