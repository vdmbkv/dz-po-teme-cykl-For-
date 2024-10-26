# "Все не так уж просто"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for numeric in numbers:

    is_prime = True

    if numeric > 1:

        for w in range(2, numeric):
            if numeric % w == 0:

                is_prime = False
                break

        if is_prime:
            primes.append(numeric)
        else:
            not_primes.append(numeric)
    elif numeric == 1:
        continue

print("Primes:", primes)
print("Not Primes:", not_primes)