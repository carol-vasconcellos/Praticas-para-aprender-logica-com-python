jogador = {"vida": 3, "pontos": 0}
print(f"Estado Inicial do Jogador: {jogador}")

print("\n--- Aumentando Pontos ---")
jogador["vid"] = jogador["pontos"] + 100
print(f"Pontos após aumento: {jogador['pontos']}")
print(f"Estado Atual: {jogador}")

print("\n--- Diminuindo a vida ---")
jogador["vida"] = jogador["vida"] - 2
print(f"Pontos após aumento: {jogador['vida']}")
print(f"Estado Atual: {jogador}")

print("\n--- Adicionando 'item' ---")
jogador["item"] = input("add: ")
print(f"Novo item adicionado: {jogador['item']}")
print(f"Estado Final do Jogador: {jogador}")