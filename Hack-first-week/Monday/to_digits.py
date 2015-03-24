def to_digits(number):
	digits = []
	while (number > 0):
		digit = number % 10
		digits.append(digit)
		number = number//10
	digits.reverse()
	return digits

print (to_digits(123))
print (to_digits(99999))