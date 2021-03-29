# find primes numbers up to n
n = int(input('number to find primes in between: '))

composites = list()
primes = list()

steps = 0
for a in range(2, n):  # begins with 2, which is not in the composites list, then, must be a prime.
    steps += 1
    if a not in composites:
        primes.append(a)

        for multiples in range(a, n):  # if a number is prime, every multiple of its number is not prime.
            steps += 1
            if multiples % a == 0:
                if multiples not in primes:  # and if a number is not prime, it is composite.
                    composites.append(multiples)

print(f"it was taken {steps} steps.")
print(primes)
print(composites)
print(f"there are {len(primes)} prime numbers in the list")
