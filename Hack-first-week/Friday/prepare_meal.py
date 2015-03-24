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
    factorization = {}
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            prime_divisors.append(i)
    for divisor in prime_divisors:
        count = 0
        while number % divisor == 0:
            count += 1
            number = number / divisor
        factorization[divisor] = count
    return factorization


def prepare_meal(number):
    resulting_string = ''
    dictionary = prime_factorization(number)
    if 3 in dictionary:
        resulting_string = 'spam ' * dictionary[3]
    if number % 5 == 0:
        resulting_string = 'eggs' if resulting_string == '' else resulting_string + 'and eggs'
    return resulting_string

print(prepare_meal(5))
print(prepare_meal(45))
print(prepare_meal(15))