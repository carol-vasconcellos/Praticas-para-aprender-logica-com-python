import random

# --- FUNÇÃO: criar tabuleiro (9 espaços vazios) ---
def criar_tabuleiro():
    return [" "] * 9


# --- FUNÇÃO: mostrar tabuleiro ---
def mostrar_tabuleiro(tab):
    print()
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
    print()


# --- COMBINAÇÕES DE VITÓRIA ---
vitorias = [
    (0,1,2), (3,4,5), (6,7,8),      # linhas
    (0,3,6), (1,4,7), (2,5,8),      # colunas
    (0,4,8), (2,4,6)                # diagonais
]


# --- FUNÇÃO: checar vencedor ---
def verificar_vencedor(tab):
    for a, b, c in vitorias:
        if tab[a] == tab[b] == tab[c] and tab[a] != " ":
            return tab[a]   # retorna "X" ou "O"
    return None


# --- FUNÇÃO: verificar empate ---
def deu_empate(tab):
    return " " not in tab


# --- FUNÇÃO: turno do jogador ---
def jogador_joga(tab):
    while True:
        pos = input("Escolha uma posição (1-9): ")

        if not pos.isdigit():
            print("Digite apenas números!")
            continue

        pos = int(pos)

        if pos < 1 or pos > 9:
            print("Posição inválida!")
            continue

        pos -= 1  # convertendo para índice 0–8

        if tab[pos] != " ":
            print("Essa posição já está ocupada!")
            continue

        tab[pos] = "X"
        break


# --- FUNÇÃO: turno da IA (básico) ---
def ia_joga(tab):
    # lista de posições vazias
    disponiveis = [i for i, val in enumerate(tab) if val == " "]

    # escolhe uma aleatória
    escolha = random.choice(disponiveis)

    tab[escolha] = "O"
    print(f"\nIA jogou na posição {escolha + 1}.\n")


# --- FUNÇÃO PRINCIPAL: loop do jogo ---
def jogar():
    tab = criar_tabuleiro()

    print("=== JOGO DA VELHA — HUMANO (X) VS IA (O) ===")

    while True:
        mostrar_tabuleiro(tab)

        # jogador joga
        jogador_joga(tab)

        winner = verificar_vencedor(tab)
        if winner:
            mostrar_tabuleiro(tab)
            print(f"🎉 Jogador {winner} venceu!")
            break

        if deu_empate(tab):
            mostrar_tabuleiro(tab)
            print("🤝 Deu empate!")
            break

        # IA joga
        ia_joga(tab)

        winner = verificar_vencedor(tab)
        if winner:
            mostrar_tabuleiro(tab)
            print(f"🤖 IA ({winner}) venceu!")
            break

        if deu_empate(tab):
            mostrar_tabuleiro(tab)
            print("🤝 Deu empate!")
            break


# --- Iniciar jogo ---
jogar()
