import WConio2 as W

'''
COR_NAIPE = {
    "copas":W.RED,
    "ouros": W.RED,
    "paus": W.BLACK,
    "espadas": W.BLACK
}

'''

naipes = {"copas": "♥", "ouros": "♦", "paus": "♣", "espadas": "♠"} #Dicionario nome do naipe e simbolo que aparece na carta
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #Lista dos valores das cartas

def montar_carta(valor, simbolo):
    topo = valor.ljust(3) # valor alinhado à esquerda ocupando (x) espaços
    base = valor.rjust(3) # valor alinhado à direita ocupando (x) espaços
    return [
         "┌───────────┐",
        f"│ {topo}       │",
        "│           │",
        "│           │",
        f"│     {simbolo}     │",
        "│           │",
        "│           │",
        f"│       {base} │",
        "└───────────┘",

    ]

baralho = {} #dicionario vazio que vai guardar as 52 cartas 
for nome_naipe, simbolo in naipes.items(): #passa por cada naipe 
    cor = W.LIGHTRED if nome_naipe in ("copas", "ouros") else W.WHITE
    for valor in valores: #passa para cada naipe, passa por todos os valores 
        baralho[f"{valor} de {nome_naipe}"] = { #entrada da carta
            "valor": valor,
            "naipe": nome_naipe,
            "cor": cor,
            "arte": montar_carta(valor, simbolo),
        }

# desenha uma carta na tela a partir do nome, na coluna x e linha y
def desenhar_carta(nome, x, y):
    carta = baralho[nome]
    for i, linha in enumerate(carta["arte"]):
        W.gotoxy(x, y + i)
        W.textcolor(carta["cor"])
        print(linha)
    W.textcolor(W.WHITE) # terminal volta para branco no final

# desenha duas cartas lado a lado: a primeira na coluna 5 e a segunda na coluna 20, ambas na linha 3
desenhar_carta("A de espadas", 5, 3)
desenhar_carta("10 de copas", 20, 3)