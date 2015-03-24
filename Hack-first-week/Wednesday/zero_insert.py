def zero_insert(number):
	number_str = str(number)
	digits = [number_str[i] for i in range(0, len(number_str))]
	indexes_of_zeros = []
	for i in range(0,len(number_str)-1):
		if number_str[i] == number_str[i+1]:
			indexes_of_zeros.append(i+1)
		else:
			if (int(number_str[i]) + int(number_str[i+1])) % 10 ==0:
				indexes_of_zeros.append(i+1)
	count = 0
	for index in indexes_of_zeros:
		digits.insert(index + count, 0)
		count += 1
	print (indexes_of_zeros)
	print(digits)


print(zero_insert(116457))
print(zero_insert(55555555))
print(zero_insert(6446))