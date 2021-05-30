def letra_aletoria(posicao=False):
    from random import randint
    alfabeto = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
    alfa_lista = alfabeto.split(" ")                                 # faz lista d0 alfabeto
    n_do_alfa = randint(0, len(alfa_lista) - 1)                      # numero aleatório de 0 ate 25 (26 numeros)
    letra_rand = alfa_lista[n_do_alfa]                               # letra na posição do numero aletório
    if posicao:
        return letra_rand, n_do_alfa + 1
    else:
        return letra_rand


def palavra_aleatoria():
    from random import randint
    palavras = ('abacate banana côco damasco eplepsia fruta gay helicóptero imbecil jegue karalho lingua micro nox ópio'
                ' panela queixo ramificação sacaralho tu ulson vaca wiiu xá yipsilon zero')
    list_palavras = palavras.split(' ')
    palavra_rand = randint(0, len(list_palavras))
    return list_palavras[palavra_rand].upper()


letraenumero = letra_aletoria(True)
print(f'A letra aleatoria: {letraenumero[0]}, de numero: {letraenumero[1]}, e uma palavra aleatoria '
      f'"{palavra_aleatoria()}"')
