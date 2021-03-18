from random import randint
playernum = 0
parouimpar = -1
playermaiscomp = 0
vitorias = 0
while True:
    compnum = randint(1, 2)
    while playernum != 2 and playernum != 1:
        playernum = int(input('2 ou 1? '))
    while parouimpar != 2 and parouimpar != 1:
        parouimpar = int(input('[2 para par] ou [1 para impar] '))
    playermaiscomp = playernum + compnum
    if parouimpar == 2:
        if playermaiscomp % 2 == 0:
            print('voce ganhou')
            vitorias += 1
            parouimpar = 0
            playernum = 0
        else:
            print('voce perdeu')
            break
    if parouimpar == 1:
        if playermaiscomp % 2 == 1:
            print('voce ganhou.')
            vitorias += 1
            parouimpar = 0
            playernum = 0
        else:
            print('voce perdeu')
            break
print(f'voce teve {vitorias} vitorias ')
