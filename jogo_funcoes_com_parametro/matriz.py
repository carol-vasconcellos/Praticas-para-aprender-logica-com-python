import random

def criar_matriz(tamanho):
    tabuleiro = [["💧" for _ in range(tamanho)] for _ in range(tamanho)]

    return tabuleiro
       

def posicionar_tesouro(tamanho):
    linha = random.randint(0, tamanho - 1)
    coluna = random.randint(0, tamanho - 1)
    return (linha, coluna)

def verificar_acerto(palpite, tesouro):
    return palpite == tesouro

def atualizar_matriz(matriz, palpite, acertou):

    linha, coluna = palpite
    
    if acertou:
        # Se acertou, marcamos com o tesouro
        matriz[linha][coluna] = '💰'
    else:
        
        if matriz[linha][coluna] == '💧':
            matriz[linha][coluna] = '💥' # Troca água por bomba (erro)

def imprimir_matriz(matriz):
    tamanho = len(matriz)
    
    # 1. Imprime o cabeçalho das colunas (0 1 2 ...)
    print("  ", end="")
    for i in range(tamanho):
        # Garante que a coluna 10 em diante não quebre o espaçamento
        print(f" {i:2}", end="") 
    print("\n  " + "---" * tamanho) 

    # 2. Imprime as linhas
    for i in range(tamanho):
        # Imprime o índice da linha
        print(f"{i:2}|", end="") 
        # Imprime os elementos da linha
        for j in range(tamanho):
            # O f-string {:2} garante 2 espaços para cada elemento
            print(f" {matriz[i][j]:2}", end="") 
        print()
