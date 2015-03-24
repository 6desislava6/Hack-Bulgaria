def sum_of_divisors(number):
    sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sum += i
    return sum


print (sum_of_divisors(8))
print (sum_of_divisors(sum_of_divisors(1000)))
