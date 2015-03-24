def contains_digit(number, digit):
	number_as_string = str(number)
	digits = [int(x) for x in number_as_string]
	print (digits)
	if digit in digits:
		return True
	else:
		return False
print(contains_digit(12346789, 5))
print(contains_digit(1000, 0))