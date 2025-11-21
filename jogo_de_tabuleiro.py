import random

def criar_matriz():
    matriz = [["_"] * 5 for _ in range(5)]

    linha = random.randint(0, 4)
    coluna = random.randint(0, 4)
    matriz[linha][coluna] = "T"
    return matriz

def jogar():
    tab = criar_matriz()

    tentativas = 0

    while True:

        print("-"* 40)
        print("Bem-vindo a caça ao tesouro. Se encontrat o 'T', você ganha!")
        print("-"* 40)

        for linha in tab:
            linha_invisivel = ["_" if c == "T" else c for c in linha]
            print(" ".join(linha_invisivel))
        print()

        opcao = input("Faça uma jogada (ex: 2 3): ").split()

        if len(opcao) != 2:
            print("Digite dois números!")
            continue

        if not opcao[0].isdigit() or not opcao[1].isdigit():
            print("Somente números!")
            continue

        linha = int(opcao[0])
        coluna = int(opcao[1])

        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            print("Fora do tabuleiro!")
            continue

        tentativas += 1

        if tentativas >= 20:
            print(f"Você chegou ao maximo das tentativas: {tentativas}")
            break

        if tab[linha][coluna] == "T":
            print("\n🎉 VOCÊ ENCONTROU O TESOURO! PARABÉNS!")

            print("Tabuleiro final:")
            for linha_final in tab:
                print(" ".join(linha_final))
            print(f"Numero de tentativas: {tentativas}")    
            break
        else:
            print("❌ Nada aqui!")
            tab[linha][coluna] = "X"
            
jogar()