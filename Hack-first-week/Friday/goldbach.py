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


def goldbach(number):
    resulting_prime_comb = ()
    for num in range(2, number // 2 + 1):
        if is_prime(num) and is_prime(number - num):
            resulting_prime_comb += ((num, number - num), )
    return resulting_prime_comb
print(goldbach(6))
print(goldbach(10))
print(goldbach(100))
