def numerosbinarios(ndecimal):
    lista_potencias = list()
    nbinario = list()

    for x in range(0, ndecimal + 1):
        potencias = 2**x
        if potencias <= ndecimal:
            lista_potencias.append(potencias)

    lista_reversa = lista_potencias[::-1]
    # print(lista_reversa)

    primeiro = numr = contador = 0

    while True:
        contador += 1
        if ndecimal == 1:
            nbinario.append(1)
            break
        elif ndecimal == 0:
            nbinario.append(0)
            break
        if primeiro == 0:
            nbinario.append(1)
            primeiro += 1

            numr = lista_reversa[0]
        if primeiro > 0:
            if numr + lista_reversa[primeiro] <= ndecimal:
                nbinario.append(1)
                numr += lista_reversa[primeiro]
                primeiro += 1

            elif numr + lista_reversa[primeiro] > ndecimal:
                nbinario.append(0)
                primeiro += 1

            if len(lista_reversa) == len(nbinario):
                break

    # print(nbinario)
    # print(f'{contador} steps')

    for f in nbinario:
        print(f, end='')


numerosbinarios(int(input('um numero em base decimal para transformar em binario: ')))
