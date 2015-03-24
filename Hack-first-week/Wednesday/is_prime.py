import math
def is_prime(number):
	bool_prime = True
	if number <= 0:
		bool_prime = False
	else:
		for i in range(1,int(number/2)):
			if number % i == 0:
				bool_prime = False
				break
	return bool_prime
