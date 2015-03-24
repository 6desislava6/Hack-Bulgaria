def contains_digits(number, digits):
	number_digits = []
	all_in = True
	while number > 0:
		number_digits.append(number%10)
		number = number // 10
	for digit in digits:
		if digit not in number_digits:
			all_in = False
			break
	return all_in

print (contains_digits(402123, [0, 3, 4]))
print (contains_digits(666, [6,4]))
print (contains_digits(123456789, [1,2,3,0]))
