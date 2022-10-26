import random
from palavras import palavras
import string

def get_palavra_valida(palavras):
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()

def forca():
    palavra = get_palavra_valida(palavras)
    letras_palavra = set(palavra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()

    while len(letras_palavra) > 0:
        print('Voce usou as seguintes letras: ', ' '.join(letras_usadas))

        lista_palavra = [letra if letra in letras_usadas else '-' for letra in palavra]
        print('Palavra atual: ', ' '.join(lista_palavra))

        letra_usada = input('Adivinhe uma letra: ').upper()
        if letra_usada in alfabeto - letras_usadas:
            letras_usadas.add(letra_usada)
            if letra_usada in letras_palavra:
                letras_palavra.remove(letra_usada)

        elif letra_usada in letras_usadas:
            print('Voce ja escolheu essa letra, tente outra!')

        else:
            print('Caracter invalido')

    print('Voce acertou a palavra ' + palavra +  '!!')

forca()
