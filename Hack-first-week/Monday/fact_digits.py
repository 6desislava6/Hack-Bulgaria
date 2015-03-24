from factorial import factorial
def fact_digits(number):
	digits = []
	sum = 0
	while (number > 0):
		digit = number % 10
		digits.append(digit)
		number = number//10
	for digit in digits:
		sum += factorial(digit)
	return sum

print (fact_digits(111))
print (fact_digits(999))
