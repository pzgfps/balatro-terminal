import random

class Coringa:
    nome = ""
    preco = 0

    def efeito(self, pontuacao, mult, descarte):
        raise NotImplementedError

class CoringaJoker(Coringa):
    nome = "Joker"
    preco = 4

    def efeito(self, pontuacao, mult, descarte):
        return mult + 4

class CoringaMisprint(Coringa):
    nome = "Erro de impressão"
    preco = 4

    def efeito(self, pontuacao, mult, descarte):
        return mult + random.randint(0, 23)

class CoringaDusk(Coringa):
    nome = "Cume Místico"
    preco = 5

    def efeito(self, pontuacao, mult, descarte):
        if descarte == 0:
            return mult + 4
        return mult

class CoringaMime(Coringa):
    nome = "Mímico"
    preco = 5

    def efeito(self, pontuacao, mult, descarte):
        return mult 