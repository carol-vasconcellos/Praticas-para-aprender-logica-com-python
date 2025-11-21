matriz = [["."] * 5 for _ in range(5)]

# SUBISTITUI ESSA PARTE POR "X"
matriz[2][3] = "X"

contador = 0

#PERCORRE A MATRIZ E A FORMATA
for linha in matriz:
    print(" ".join(linha))
print()

# Para ver quantos "."" existem
for linha in matriz:
    for celula in linha:
        if celula == ".":
            contador += 1

print("Quantidade de pontos:", contador )
print()

def criar_matriz(n, m, valor):
    matriz = [[valor] * m for _ in range(n)]
    return matriz

matriz = criar_matriz(5,5,"*")

for linha in matriz:
    print(" ".join(linha))
print()