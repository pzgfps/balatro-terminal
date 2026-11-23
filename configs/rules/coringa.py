import random

class Coringa:      # o "molde" de todos os coringas: cada coringa herda dessa classe e sobrescreve so o que ele faz
    nome = ""
    preco = 0

    def efeito_fichas(self, fichas, descartes):     # devolve as fichas novas. O padrao é nao mexer em nada
        return fichas

    def efeito_mult(self, mult, descartes):         # devolve o mult novo. O padrao é nao mexer em nada
        return mult                                 # assim um coringa so de mult nao precisa escrever efeito_fichas (e vice-versa)

class CoringaJoker(Coringa):
    nome = "Joker"
    preco = 4

    def efeito_mult(self, mult, descartes):
        return mult + 4             # soma 4 no mult (+4 Mult, nao multiplica)

class CoringaMisprint(Coringa):
    nome = "Erro de impressão"
    preco = 4

    def efeito_mult(self, mult, descartes):
        return mult + random.randint(0, 23)     # sorteia um numero de 0 a 23 (os dois entram) e soma no mult, muda a cada jogada

class CoringaMysticSummit(Coringa):
    nome = "Cume Místico"
    preco = 5

    def efeito_mult(self, mult, descartes):
        if descartes == 0:           # so funciona quando o jogador nao tem mais nenhum descarte
            return mult + 15        # nesse caso soma 15 no mult
        return mult                 # se ainda tem descarte, nao muda nada

class CoringaCavendish(Coringa):
    nome = "Cavendish"
    preco = 4

    def efeito_mult(self, mult, descartes):
        return mult * 3             # MULTIPLICA o mult por 3 (X3 Mult), por isso cresce bem mais rapido que os de somar
                                    # no jogo de verdade ele tem 1 chance em 1000 de se destruir no fim da rodada, aqui ainda nao

class CoringaMime(Coringa):
    nome = "Mímico"
    preco = 5
                                    # no jogo de verdade ele repete efeitos de cartas que ficam na mao, mas aqui ainda nao tem nada pra repetir
                                    # (sem efeito por enquanto: usa o padrao do molde, que nao mexe em nada)

#class CoringaBluePrint(Coringa):