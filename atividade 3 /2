import random

def escolhePalavra():
    palavras = ['caixa', 'dedo', 'computador', 'carro', 'manga']
    return random.choice(palavras)

def forca():
    palavra = escolhePalavra()
    palavraEscondida = ['_'] * len(palavra)
    chances = 7
    letraErradas = []

    print("Bem-vindo ao jogo da Forca!")
    print("Adivinhe a palavra secreta. Ela tem", len(palavra), "letras.")

    while chances > 0:
        print("Palavra: ", " ".join(palavraEscondida))
        print("Chances restantes:", chances)
        print("Letras erradas:", ", ".join(letraErradas))

        tentativa = input("Digite uma letra ou a palavra completa: ").lower()

        if len(tentativa) == 1:  
            if tentativa in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == tentativa:
                        palavraEscondida[i] = tentativa
                if '_' not in palavraEscondida:
                    print("Parabéns! Você acertou a palavra:", palavra)
                    return
            else:
                letraErradas.append(tentativa)
                chances -= 1
        else:  
            if tentativa == palavra:
                print("Parabéns! Você acertou a palavra:")
                return
            else:
                chances -= 1

    print("Você perdeu! A palavra correta era:", palavra)

forca()

