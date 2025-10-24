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
            for posicao in posicoes:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
    return tabuleiro