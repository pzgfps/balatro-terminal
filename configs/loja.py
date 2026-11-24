import random                                       # sorteia os coringas da loja
from configs.rules.coringa import CoringaJoker, CoringaMisprint, CoringaMysticSummit, CoringaCavendish, CoringaMime

# este arquivo so tem logica (nada de print nem de tela): quem faz a tela so precisa chamar essas funcoes
#
# o dicionario "loja" tem o mesmo formato que a tela (assets/art/menu_compra.py) ja le:
#   {"reroll": preco, "itens": [item, item], "voucher": item, "pacotes": [item, item]}
# onde item = {"nome": ..., "tipo": ..., "preco": ...}
# por enquanto a loja so vende CORINGAS e tem o Reroll: o voucher e os pacotes ficam indisponiveis (preco impossivel de pagar,
# entao a tela mostra eles em cinza e ignora o clique). Quando o grupo quiser, e so trocar por itens de verdade.

CATALOGO = [CoringaJoker, CoringaMisprint, CoringaMysticSummit, CoringaCavendish, CoringaMime]   # coringas que podem aparecer
PRECO_REROLL = 5            # quanto custa o primeiro reroll de cada visita a loja
ACRESCIMO_REROLL = 1        # cada reroll na mesma visita fica $1 mais caro
MAX_CORINGAS = 5            # quantos coringas o jogador pode ter ao mesmo tempo
PRECO_INDISPONIVEL = 999    # preco de um espaco que nao esta a venda (ninguem tem esse dinheiro)

# ----------------------------------------------------Montar a loja-------------------------------------------------------------#

def item_indisponivel(nome):                        # espaco vazio: a tela precisa que o slot exista, entao ele fica "trancado"
    return {"nome": nome, "tipo": "", "preco": PRECO_INDISPONIVEL}

def sortear_item():                                 # escolhe um coringa do catalogo e monta o item que a tela mostra
    classe = random.choice(CATALOGO)                # a classe do coringa (ainda nao e o coringa em si)
    return {"nome": classe.nome, "tipo": "Coringa", "preco": classe.preco, "classe": classe}    # guarda a classe pra criar o coringa na compra

def gerar_loja(rerolls_feitos=0):                   # monta uma loja nova / rerolls_feitos so serve pra calcular o preco do reroll
    return {
        "reroll": PRECO_REROLL + ACRESCIMO_REROLL * rerolls_feitos,     # reroll 1 = $5, reroll 2 = $6, reroll 3 = $7...
        "rerolls_feitos": rerolls_feitos,
        "itens": [sortear_item(), sortear_item()],                      # 2 coringas a venda
        "voucher": item_indisponivel("Voucher"),                        # ainda nao existe
        "pacotes": [item_indisponivel("Pacote"), item_indisponivel("Pacote")],   # ainda nao existe
    }

# ------------------------------------------------------------------------------------------------------------------------------#

# ----------------------------------------------------Comprar e rerrolar--------------------------------------------------------#
# as funcoes abaixo devolvem um texto dizendo o que aconteceu, pra tela poder avisar o jogador:
#   "ok", "sem_dinheiro", "sem_espaco", "indisponivel"

def comprar_item(partida, loja, indice):            # indice: 0 ou 1 (qual dos 2 itens)
    item = loja["itens"][indice]
    if "classe" not in item:                        # espaco vazio (ja vendido): nao tem o que comprar
        return "indisponivel"
    if len(partida.coringas) >= MAX_CORINGAS:       # ja tem 5 coringas
        return "sem_espaco"
    if partida.estado.dinheiro < item["preco"]:     # nao tem dinheiro
        return "sem_dinheiro"
    partida.estado.dinheiro -= item["preco"]        # paga
    partida.coringas.append(item["classe"]())       # a classe com () cria o coringa e entra na lista que a pontuacao usa
    loja["itens"][indice] = item_indisponivel("Vendido")    # o slot fica "Vendido" (a tela continua com os 2 slots)
    return "ok"

def rerrolar_loja(partida, loja):                   # troca os coringas a venda, gastando o preco do reroll
    if partida.estado.dinheiro < loja["reroll"]:
        return "sem_dinheiro"
    partida.estado.dinheiro -= loja["reroll"]       # paga
    loja.update(gerar_loja(loja["rerolls_feitos"] + 1))     # sorteia de novo e o proximo reroll fica $1 mais caro
    return "ok"

def aplicar_acao(partida, loja, acao, indice):      # recebe o que a tela devolveu, ex: ("item", 0), e executa
    if acao == "proxima":                           # sair da loja: a tela depois chama iniciar_blind_atual() do rodada.py
        return "proxima"
    if acao == "item":
        return comprar_item(partida, loja, indice)
    if acao == "reroll":
        return rerrolar_loja(partida, loja)
    return "indisponivel"                           # voucher e pacote ainda nao existem

# ------------------------------------------------------------------------------------------------------------------------------#
