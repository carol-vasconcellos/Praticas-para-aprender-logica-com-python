import random

estado_jogador = {
    "vida": 100,
    "energia": 100,
    "inventario": ["martelo", "espada"],
    "posicao": (0, 0),
    "poderes": {"super_forca", "teletransporte"}
}

vida = estado_jogador["vida"]
print(f"Sua vida atual é: {vida}")

energia = estado_jogador["energia"]
print(f"Sua energia atual é: {energia}")

inventario = estado_jogador["inventario"]
print(f"Seu inventario atual é: {inventario}")

posicao = estado_jogador["posicao"]
print(f"Sua posição atual é: {posicao}")

poderes = estado_jogador["poderes"]
print(f"Seus poderes atuais são: {poderes}")

interacao = int(input("Você perdeu quantos de vida? "))

estado_jogador["vida"] -= interacao

print(f"Sua vida atual: {estado_jogador['vida']}")

intera = input("O que quer colcoa no inventario: ")

estado_jogador["inventario"].append(intera)

print(f"Seu inventario atual: {estado_jogador['inventario']}")

# MOVER JOGADOR
print(f"Posição inicial: {estado_jogador['posicao']}")

direcao = input("Mover (w=up, a=left, s=down, d=right): ")

x, y = estado_jogador["posicao"]

if direcao == "w":
    y -= 1
elif direcao == "s":
    y += 1
elif direcao == "a":
    x -= 1
elif direcao == "d":
    x += 1
else:
    print("Direção inválida!")

estado_jogador["posicao"] = (x, y)

print(f"Nova posição: {estado_jogador['posicao']}")

def jogador():
    global estado_jogador

    print("Aqui seu status atual")
    print("Sua vida atual: ", estado_jogador["vida"])
    print("Sua energia atual: ", estado_jogador["energia"])
    print("Seu inventario  atual: ", ", ".join(estado_jogador["inventario"]))
    print("Sua posição atual: ", estado_jogador["posicao"])
    print("Seus poderes atuais: ", ", ".join(estado_jogador["poderes"]))

jogador()