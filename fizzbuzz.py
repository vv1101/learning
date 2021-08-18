fizz = []
buzz = []
fizzbuzz = []
for x in range(1, 101):
    n = ''
    if x % 3 == 0:
        n += 'fizz'
        fizz.append(n)
    if x % 5 == 0 and x % 3 != 0:
        buzz.append('buzz')
    if x % 5 == 0:
        n += 'buzz'
    if n == 'fizzbuzz':
        fizzbuzz.append('fizzbuzz')
    if x % 5 != 0 and x % 3 != 0:
        n = x
    print(n)
print(len(fizz))
print(len(buzz))
print(len(fizzbuzz))
