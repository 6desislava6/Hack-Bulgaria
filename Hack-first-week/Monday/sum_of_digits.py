def sum_of_digits(number):
	sum = 0
	number = abs (number)
	while (number > 0):
		sum += number % 10
		number = number//10
	return sum
print (sum_of_digits(1325132435356))
print (sum_of_digits(-10))
print (sum_of_digits(123))