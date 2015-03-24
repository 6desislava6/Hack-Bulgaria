def fibonacci(number):
	if number < 0:
		return "Not correct!"
	elif number == 1:
		return 1
	elif number == 2:
		return [1, 1]
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
		return numbers;
print(fibonacci(10))