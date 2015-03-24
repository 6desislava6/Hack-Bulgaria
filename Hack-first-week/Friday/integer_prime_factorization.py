def is_prime(number):
    bool_prime = True
    if number <= 0:
        bool_prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                bool_prime = False
                break
    return bool_prime


def prime_factorization(number):
    prime_divisors = []
    factorization = ()
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_divisors.append(i)
    for divisor in prime_divisors:
        count = 0
        while number % divisor == 0:
            count += 1
            number = number / divisor
        factorization += ((divisor, count),)
    print(prime_divisors)
    return factorization

print(prime_factorization(10))
print(prime_factorization(356))
