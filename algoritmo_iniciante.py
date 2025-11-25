# ✔ Ex 1 — Contar quantos “X” existem na matriz
matriz = [
    ['~', 'X', '~'],
    ['X', '~', 'X'],
    ['~', '~', 'X']
]

caractere_a_contar = 'X'
contador_total = 0

for linha in matriz:
    contagem_na_linha = linha.count(caractere_a_contar)
    
    contador_total += contagem_na_linha

print("\n--- Contagem de Caractere ---")
print(f"O caractere '{caractere_a_contar}' aparece {contador_total} vezes na matriz.")

# ✔ Ex 2 — Encontrar todas as coordenadas de um item
matriz = [
    ['~', 'X', '~'],
    ['X', '~', 'X'],
    ['~', '~', 'X']
]

item_procurado = 'X'
coordenadas_encontradas = []

for i, linha in enumerate(matriz):
    for j, item in enumerate(linha):
        
        if item == item_procurado:
            coordenadas_encontradas.append((i, j))

print(f"O item '{item_procurado}' foi encontrado nas coordenadas:")
print(coordenadas_encontradas)

# ✔ Validar vitória (Lógica de Jogo da Velha/Padrões)

def verificar_vitoria_combinacoes(movimentos_do_jogador, combinacoes_vencedoras):
   
    for combinacao in combinacoes_vencedoras:
        
        todos_presentes = True 
        
        for coordenada_necessaria in combinacao:
            
            if coordenada_necessaria not in movimentos_do_jogador:
                todos_presentes = False 
                break 
        
        if todos_presentes:
            return True 

    return False

combinacoes_vencedoras = [
    ((0, 0), (1, 1), (2, 2)), 
    ((0, 0), (0, 1), (0, 2)), 
]

movimentos_vencedores = [(0, 0), (1, 1), (2, 2), (0, 1)] 
venceu = verificar_vitoria_combinacoes(movimentos_vencedores, combinacoes_vencedoras)

print("\n--- Validação de Vitória ---")
print(f"O jogador venceu? {venceu}")
