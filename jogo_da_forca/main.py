import random


def escolher_palavra():
    palavras = ['cachorro', 'gato', 'elefante', 'cavalo', 'papagaio']
    return random.choice(palavras)


def jogar():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    letras_erradas = set()
    tentativas = 6

    while tentativas > 0:
        palavra_lista = [letra if letra in letras_adivinhadas else '_' for letra in palavra]
        print('Palavra:', ' '.join(palavra_lista))

        if '_' not in palavra_lista:
            print('Parabéns! Você ganhou!')
            break

        print(f'Tentativas restantes: {tentativas}')
        print('Letras erradas:', ' '.join(letras_erradas))

        tentativa = input('Adivinhe uma letra: ').lower()

        if tentativa in letras_adivinhadas or tentativa in letras_erradas:
            print('Você já tentou essa letra.')
            continue

        if tentativa in palavra:
            letras_adivinhadas.add(tentativa)
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1

        if tentativas == 0:
            print('Você perdeu! A palavra era:', palavra)


if __name__ == '__main__':
    jogar()
