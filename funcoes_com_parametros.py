def processar_string(texto):
    minuscula = texto.lower()
    maiuscula = texto.upper()
    tamanho = len(texto)

    return (minuscula, maiuscula, tamanho)

print(processar_string("Isso é um teste"))


#simular tabuleiro 5x5

print(*('x' * 5 for _ in range(5)), sep='\n')

# Versão correta e didática (melhor para estudo)
def criar_tabuleiro(n):
    for _ in range(n):
        print("x " * n)

criar_tabuleiro(5)

# Versão profissional usando matriz
def criar_tabuleiro(n):
    tabuleiro = [["x"] * n for _ in range(n)]
    
    for linha in tabuleiro:
        print(" ".join(linha))

criar_tabuleiro(5)
