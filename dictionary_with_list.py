inventario = {
    "armas": ["espada", "arco"],
    "itens": ["cura", "mana"]
}

inventario["armas"].remove("arco")
print(inventario)

inventario["armas"].append("pistola")
print(inventario)

print("\n--- Percorrendo Categorias e Itens ---")
# 1. Percorre as chaves (categorias) e os valores (listas de itens)
for categoria, lista_de_itens in inventario.items():
    print(f"Categoria: {categoria.upper()} {lista_de_itens}")
    