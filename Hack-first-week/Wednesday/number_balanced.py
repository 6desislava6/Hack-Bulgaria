def is_number_balanced(number):

	if number < 10:
		return True
	else:
		len_number = len(str(number))
		half_digits = len_number//2
		digits = make_digits(number)
		print (digits)
		sum1 = 0
		sum2 = 0
		for i in range(0,half_digits):
			sum1 += digits[i]
			sum2 += digits[len_number-1-i]
		return (sum1 == sum2)

def make_digits (number):
	number_digits = []
	while number > 0:
		number_digits.append(number%10)
		number = number // 10
	return number_digits[::-1]
print(is_number_balanced(121))
print(is_number_balanced(4518))
print(is_number_balanced(28471))