from random import randrange

digitos = 50
senha = []

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symb = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '=', '+', '<', '.', '>', '/', '?']


for a in range(0, digitos):
    coisa = randrange(1, 5, 1)
    if coisa == 1:
        senha.append(alfa[randrange(0, len(alfa), 1)])
    if coisa == 4:
        senha.append(alfa[randrange(0, len(alfa), 1)])
        print(senha)
    if coisa == 2:
        senha.append(num[randrange(0, len(num), 1)])
        print(senha)
    if coisa == 3:
        senha.append(symb[randrange(0, len(symb), 1)])
        print(senha)
for letra in senha:
    print(letra, end='')
print(f'\n{len(senha)}')
