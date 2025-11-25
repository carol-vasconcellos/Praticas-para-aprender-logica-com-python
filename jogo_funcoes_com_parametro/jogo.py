import jogo_funcoes_com_parametro.matriz as matriz

TAMANHO_MATRIZ = 5  
TENTATIVAS_MAXIMAS = 10

def obter_palpite(tamanho):
    while True:
        try:
            # Pede a entrada no formato "linha,coluna"
            entrada = input(f"Digite as coordenadas (linha,coluna de 0 a {tamanho - 1}): ")
            
            # Divide a string em dois valores
            partes = entrada.split(',')
            if len(partes) != 2:
                raise ValueError("Formato incorreto. Use 'linha,coluna'.")
            
            # Converte para inteiros
            linha = int(partes[0].strip())
            coluna = int(partes[1].strip())
            
            # Verifica se estão dentro do limite da matriz
            if 0 <= linha < tamanho and 0 <= coluna < tamanho:
                return (linha, coluna)
            else:
                print(f"Coordenadas fora do limite! Use valores entre 0 e {tamanho - 1}.")
        except ValueError as e:
            print(f"Entrada inválida. {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def jogar():
    print("🚢 Bem-vindo à Caça ao Tesouro!")
    print(f"Tente encontrar o tesouro '💰' na grade {TAMANHO_MATRIZ}x{TAMANHO_MATRIZ} em {TENTATIVAS_MAXIMAS} tentativas.")
    print("O '~' é água não explorada, e o 'X' é onde você errou.")
    print("-" * 30)

    # 1. Configuração inicial
    grade = matriz.criar_matriz(TAMANHO_MATRIZ)
    coordenadas_tesouro = matriz.posicionar_tesouro(TAMANHO_MATRIZ)
  
    
    tentativas = 0
    acertou = False
    
    # 2. Loop principal do jogo
    while tentativas < TENTATIVAS_MAXIMAS and not acertou:
        matriz.imprimir_matriz(grade)
        print(f"\nTentativa {tentativas + 1} de {TENTATIVAS_MAXIMAS}.")
        
        palpite = obter_palpite(TAMANHO_MATRIZ)
        
       
        acertou = matriz.verificar_acerto(palpite, coordenadas_tesouro)
        matriz.atualizar_matriz(grade, palpite, acertou)
        
        if acertou:
            print("🎉 Parabéns! Você encontrou o Tesouro!")
            matriz.imprimir_matriz(grade)
        else:
            print("💧 Erro! Você acertou a água. Tente novamente.")
            tentativas += 1

    # 4. Fim do Jogo
    if not acertou:
        print("\nGame Over! 😭 Suas tentativas acabaram.")
        
        print(f"O tesouro estava em: {coordenadas_tesouro}")
        
        grade_final = [row[:] for row in grade]
        matriz.atualizar_matriz(grade_final, coordenadas_tesouro, True)
        matriz.imprimir_matriz(grade_final)

# Garante que a função 'jogar' só seja chamada quando o arquivo 'jogo.py' for executado diretamente
if __name__ == "__main__":
    jogar()