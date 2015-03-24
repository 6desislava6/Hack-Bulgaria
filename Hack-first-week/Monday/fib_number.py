def fib_number(number):
	if number == 1:
		return 1
	elif number == 2:
		return 11
	else:
		first_number = 1
		second_number = 1
		numbers = [1, 1]
		while len(numbers) <= number - 2:
			swap = first_number
			first_number = first_number + second_number
			second_number = second_number + first_number
			numbers.append(first_number)
			numbers.append(second_number)
			result = ""
		for num in numbers:
			result += str(num)
		return int(result)

print (fib_number(10))