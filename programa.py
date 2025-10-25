def posiciona_frota_terminal():
    embarcacoes = [
        ("porta-avioes", 4, 1),
        ("navio-tanque", 3, 2),
        ("contratorpedeiro", 2, 3),
        ("submarino", 1, 4)
    ]

    frota = {
        "porta-avioes": [],
        "navio-tanque": [],
        "contratorpedeiro": [],
        "submarino": []
    }

    for nome, tamanho, quantidade in embarcacoes:
        for _ in range(quantidade):
            posicao_valida_encontrada = False

            while not posicao_valida_encontrada:
                print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
                linha = int(input("Linha: "))
                coluna = int(input("Coluna: "))

                if tamanho == 1:
                    orientacao = "horizontal"
                else:
                    print("[1] Vertical [2] Horizontal >", end="")
                    opc = int(input())
                    if opc == 1:
                        orientacao = "vertical"
                    else:
                if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                    preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                    posicao_valida_encontrada = True
                else:
                    print("Esta posição não está válida!")

    print(frota)

posiciona_frota_terminal()
