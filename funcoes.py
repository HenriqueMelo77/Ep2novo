def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicao = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            lista_posicao.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for j in range(tamanho):
            lista_posicao.append([linha, coluna + j])
        
    return lista_posicao

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    lista_posicao = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio in frota:
        frota[nome_navio].append(lista_posicao)
    
    else:
        frota[nome_navio] = [lista_posicao]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]

    for nome_navio in frota:
        for posicoes in frota[nome_navio]:
            for linha, coluna in posicoes:
                tabuleiro[linha][coluna] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    ja_afundou = 0

    for navios in frota.values():
        for posicoes in navios:
            afundou = True
            for linha, coluna in posicoes:
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
            if afundou:
                ja_afundou += 1

    return ja_afundou
