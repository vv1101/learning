def threexplusone(x):
    numberstoend = list()
    numberstoend.append(x)
    while numberstoend[-1] != 1:
        if x % 2 == 0:
            second = x // 2
            numberstoend.append(second)
        else:
            second = (x * 3) + 1
            numberstoend.append(second)
        x = second
    print(numberstoend)


threexplusone(10**100)
