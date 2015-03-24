from is_prime import is_prime
def count_divisors(number):
	count = 0
	for i in range(1, number + 1):
		if number%i == 0:
			count += 1
	return count
def prime_number_of_divisors(number):
	return is_prime(count_divisors(number))

print (prime_number_of_divisors(7))
print (prime_number_of_divisors(8))
print (prime_number_of_divisors(9))
		