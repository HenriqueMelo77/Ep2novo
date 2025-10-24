def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicao = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            lista_posicao.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for j in range(tamanho):
            lista_posicao.append([linha, coluna + j])
        
    return lista_posicao