from dataclasses import dataclass
import random

@dataclass
class Carta:
    valor: str                      #2, 3, 4, 5, 6, 7, 8, 9, 10, Q, J, K, A
    naipe: str                      #espadas, copas, ouros, paus

    def descricao(self):            #função inutil por enquanto, ela é basicamente um Getter, devolve as informações da carta
        return f"{self.valor} de {self.naipe}"    

    def desenhar(self):             #Desenha a carta inteira
        for linha in CARTAS[(self.valor, self.naipe)]:
            print(linha)

    def linhas(self):               #Desenha a carta linha por linha permitindo printar cartas uma do lado da outra
        return CARTAS[(self.valor, self.naipe)]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                                    #Desenhos das cartas separados por ESPADAS, COPAS, OUROS, PAUS

CORINGA = [
    r" _____ ",
    r"|Joker|",
    r"|==%, |",
    r"| \/>\|",
    r"| _>^^|",
    r"|/_\/_|",
]

CARTAS = {
    # ===== ESPADAS (♠) =====
    ("2", "espadas"): [                     #Essa linha representa uma tupla (uma lista com valores que não podem ser alterados)
        r" _____ ",                          #Ou seja, para podermos acessar essa carta (2 de espadas), precisamos inserir a tupla "2", "espadas",
        r"|2    |",                         #como se fossem duas chaves primárias no contexto de banco de dados. Isso se chama HashMap ou dicionário (no Python)
        r"|  ♠  |",
        r"|     |",
        r"|  ♠  |",
        r"|____Z|",
    ],
    ("3", "espadas"): [
        r" _____ ",
        r"|3    |",
        r"| ♠ ♠ |",
        r"|     |",
        r"|  ♠  |",
        r"|____E|",
    ],
    ("4", "espadas"): [
        r" _____ ",
        r"|4    |",
        r"| ♠ ♠ |",
        r"|     |",
        r"| ♠ ♠ |",
        r"|____h|",
    ],
    ("5", "espadas"): [
        r" _____ ",
        r"|5    |",
        r"| ♠ ♠ |",
        r"|  ♠  |",
        r"| ♠ ♠ |",
        r"|____S|",
    ],
    ("6", "espadas"): [
        r" _____ ",
        r"|6    |",
        r"| ♠ ♠ |",
        r"| ♠ ♠ |",
        r"| ♠ ♠ |",
        r"|____9|",
    ],
    ("7", "espadas"): [
        r" _____ ",
        r"|7    |",
        r"| ♠ ♠ |",
        r"|♠ ♠ ♠|",
        r"| ♠ ♠ |",
        r"|____L|",
    ],
    ("8", "espadas"): [
        r" _____ ",
        r"|8    |",
        r"|♠ ♠ ♠|",
        r"| ♠ ♠ |",
        r"|♠ ♠ ♠|",
        r"|____8|",
    ],
    ("9", "espadas"): [
        r" _____ ",
        r"|9    |",
        r"|♠ ♠ ♠|",
        r"|♠ ♠ ♠|",
        r"|♠ ♠ ♠|",
        r"|____6|",
    ],
    ("10", "espadas"): [
        r" _____ ",
        r"|10 ♠ |",
        r"|♠ ♠ ♠|",
        r"|♠ ♠ ♠|",
        r"|♠ ♠ ♠|",
        r"|___0I|",
    ],
    ("J", "espadas"): [
        r" _____ ",
        r"|J  ww|",
        r"| ♠ {)|",
        r"|(♠)% |",
        r"| ♠ % |",
        r"|__%%[|",
    ],
    ("Q", "espadas"): [
        r" _____ ",
        r"|Q  ww|",
        r"| ♠ {(|",
        r"|(♠)%%|",
        r"| ♠%%%|",
        r"|_%%%O|",
    ],
    ("K", "espadas"): [
        r" _____ ",
        r"|K  WW|",
        r"| ♠ {)|",
        r"|(♠)%%|",
        r"| ♠%%%|",
        r"|_%%%>|",
    ],
    ("A", "espadas"): [
        r" _____ ",
        r"|A    |",
        r"|     |",
        r"|  ♠  |",
        r"|     |",
        r"|____V|",
    ],

    # ===== COPAS (♥) =====
    ("2", "copas"): [
        r" _____ ",
        r"|2    |",
        r"|  ♥  |",
        r"|     |",
        r"|  ♥  |",
        r"|____Z|",
    ],
    ("3", "copas"): [
        r" _____ ",
        r"|3    |",
        r"| ♥ ♥ |",
        r"|     |",
        r"|  ♥  |",
        r"|____E|",
    ],
    ("4", "copas"): [
        r" _____ ",
        r"|4    |",
        r"| ♥ ♥ |",
        r"|     |",
        r"| ♥ ♥ |",
        r"|____h|",
    ],
    ("5", "copas"): [
        r" _____ ",
        r"|5    |",
        r"| ♥ ♥ |",
        r"|  ♥  |",
        r"| ♥ ♥ |",
        r"|____S|",
    ],
    ("6", "copas"): [
        r" _____ ",
        r"|6    |",
        r"| ♥ ♥ |",
        r"| ♥ ♥ |",
        r"| ♥ ♥ |",
        r"|____9|",
    ],
    ("7", "copas"): [
        r" _____ ",
        r"|7    |",
        r"| ♥ ♥ |",
        r"|♥ ♥ ♥|",
        r"| ♥ ♥ |",
        r"|____L|",
    ],
    ("8", "copas"): [
        r" _____ ",
        r"|8    |",
        r"|♥ ♥ ♥|",
        r"| ♥ ♥ |",
        r"|♥ ♥ ♥|",
        r"|____8|",
    ],
    ("9", "copas"): [
        r" _____ ",
        r"|9    |",
        r"|♥ ♥ ♥|",
        r"|♥ ♥ ♥|",
        r"|♥ ♥ ♥|",
        r"|____6|",
    ],
    ("10", "copas"): [
        r" _____ ",
        r"|10 ♥ |",
        r"|♥ ♥ ♥|",
        r"|♥ ♥ ♥|",
        r"|♥ ♥ ♥|",
        r"|___0I|",
    ],
    ("J", "copas"): [
        r" _____ ",
        r"|J  ww|",
        r"| ♥ {)|",
        r"|(♥)% |",
        r"| ♥ % |",
        r"|__%%[|",
    ],
    ("Q", "copas"): [
        r" _____ ",
        r"|Q  ww|",
        r"| ♥ {(|",
        r"|(♥)%%|",
        r"| ♥%%%|",
        r"|_%%%O|",
    ],
    ("K", "copas"): [
        r" _____ ",
        r"|K  WW|",
        r"| ♥ {)|",
        r"|(♥)%%|",
        r"| ♥%%%|",
        r"|_%%%>|",
    ],
    ("A", "copas"): [
        r" _____ ",
        r"|A    |",
        r"|     |",
        r"|  ♥  |",
        r"|     |",
        r"|____V|",
    ],

    # ===== OUROS (♦) =====
    ("2", "ouros"): [
        r" _____ ",
        r"|2    |",
        r"|  ♦  |",
        r"|     |",
        r"|  ♦  |",
        r"|____Z|",
    ],
    ("3", "ouros"): [
        r" _____ ",
        r"|3    |",
        r"| ♦ ♦ |",
        r"|     |",
        r"|  ♦  |",
        r"|____E|",
    ],
    ("4", "ouros"): [
        r" _____ ",
        r"|4    |",
        r"| ♦ ♦ |",
        r"|     |",
        r"| ♦ ♦ |",
        r"|____h|",
    ],
    ("5", "ouros"): [
        r" _____ ",
        r"|5    |",
        r"| ♦ ♦ |",
        r"|  ♦  |",
        r"| ♦ ♦ |",
        r"|____S|",
    ],
    ("6", "ouros"): [
        r" _____ ",
        r"|6    |",
        r"| ♦ ♦ |",
        r"| ♦ ♦ |",
        r"| ♦ ♦ |",
        r"|____9|",
    ],
    ("7", "ouros"): [
        r" _____ ",
        r"|7    |",
        r"| ♦ ♦ |",
        r"|♦ ♦ ♦|",
        r"| ♦ ♦ |",
        r"|____L|",
    ],
    ("8", "ouros"): [
        r" _____ ",
        r"|8    |",
        r"|♦ ♦ ♦|",
        r"| ♦ ♦ |",
        r"|♦ ♦ ♦|",
        r"|____8|",
    ],
    ("9", "ouros"): [
        r" _____ ",
        r"|9    |",
        r"|♦ ♦ ♦|",
        r"|♦ ♦ ♦|",
        r"|♦ ♦ ♦|",
        r"|____6|",
    ],
    ("10", "ouros"): [
        r" _____ ",
        r"|10 ♦ |",
        r"|♦ ♦ ♦|",
        r"|♦ ♦ ♦|",
        r"|♦ ♦ ♦|",
        r"|___0I|",
    ],
    ("J", "ouros"): [
        r" _____ ",
        r"|J  ww|",
        r"| ♦ {)|",
        r"|(♦)% |",
        r"| ♦ % |",
        r"|__%%[|",
    ],
    ("Q", "ouros"): [
        r" _____ ",
        r"|Q  ww|",
        r"| ♦ {(|",
        r"|(♦)%%|",
        r"| ♦%%%|",
        r"|_%%%O|",
    ],
    ("K", "ouros"): [
        r" _____ ",
        r"|K  WW|",
        r"| ♦ {)|",
        r"|(♦)%%|",
        r"| ♦%%%|",
        r"|_%%%>|",
    ],
    ("A", "ouros"): [
        r" _____ ",
        r"|A    |",
        r"|     |",
        r"|  ♦  |",
        r"|     |",
        r"|____V|",
    ],

    # ===== PAUS (♣) =====
    ("2", "paus"): [
        r" _____ ",
        r"|2    |",
        r"|  ♣  |",
        r"|     |",
        r"|  ♣  |",
        r"|____Z|",
    ],
    ("3", "paus"): [
        r" _____ ",
        r"|3    |",
        r"| ♣ ♣ |",
        r"|     |",
        r"|  ♣  |",
        r"|____E|",
    ],
    ("4", "paus"): [
        r" _____ ",
        r"|4    |",
        r"| ♣ ♣ |",
        r"|     |",
        r"| ♣ ♣ |",
        r"|____h|",
    ],
    ("5", "paus"): [
        r" _____ ",
        r"|5    |",
        r"| ♣ ♣ |",
        r"|  ♣  |",
        r"| ♣ ♣ |",
        r"|____S|",
    ],
    ("6", "paus"): [
        r" _____ ",
        r"|6    |",
        r"| ♣ ♣ |",
        r"| ♣ ♣ |",
        r"| ♣ ♣ |",
        r"|____9|",
    ],
    ("7", "paus"): [
        r" _____ ",
        r"|7    |",
        r"| ♣ ♣ |",
        r"|♣ ♣ ♣|",
        r"| ♣ ♣ |",
        r"|____L|",
    ],
    ("8", "paus"): [
        r" _____ ",
        r"|8    |",
        r"|♣ ♣ ♣|",
        r"| ♣ ♣ |",
        r"|♣ ♣ ♣|",
        r"|____8|",
    ],
    ("9", "paus"): [
        r" _____ ",
        r"|9    |",
        r"|♣ ♣ ♣|",
        r"|♣ ♣ ♣|",
        r"|♣ ♣ ♣|",
        r"|____6|",
    ],
    ("10", "paus"): [
        r" _____ ",
        r"|10 ♣ |",
        r"|♣ ♣ ♣|",
        r"|♣ ♣ ♣|",
        r"|♣ ♣ ♣|",
        r"|___0I|",
    ],
    ("J", "paus"): [
        r" _____ ",
        r"|J  ww|",
        r"| ♣ {)|",
        r"|(♣)% |",
        r"| ♣ % |",
        r"|__%%[|",
    ],
    ("Q", "paus"): [
        r" _____ ",
        r"|Q  ww|",
        r"| ♣ {(|",
        r"|(♣)%%|",
        r"| ♣%%%|",
        r"|_%%%O|",
    ],
    ("K", "paus"): [
        r" _____ ",
        r"|K  WW|",
        r"| ♣ {)|",
        r"|(♣)%%|",
        r"| ♣%%%|",
        r"|_%%%>|",
    ],
    ("A", "paus"): [
        r" _____ ",
        r"|A    |",
        r"|     |",
        r"|  ♣  |",
        r"|     |",
        r"|____V|",
    ],

}






"""import WConio2 as W

naipes = {"copas": "♥", "ouros": "♦", "paus": "♣", "espadas": "♠"} #Dicionario nome do naipe e simbolo que aparece na carta
valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] #Lista dos valores das cartas

def montar_carta(valor, simbolo):
    topo = valor.ljust(3) # valor alinhado à esquerda ocupando (x) espaços
    base = valor.rjust(3) # valor alinhado à direita ocupando (x) espaços
    return [
           "┌─────────────┐",
        f"│ {topo}         │",
        "│             │",
        "│             │",
        "│             │",
        f"│      {simbolo}      │",
        "│             │",
        "│             │",
        "│             │",
        f"│         {base} │",
        "└─────────────┘",

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
desenhar_carta("10 de copas", 20, 3)"""