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
    if tabuleiro[linha][coluna] == 'n':
        tabuleiro[linha][coluna] = 'x'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro