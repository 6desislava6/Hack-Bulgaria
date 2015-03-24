def to_number(digits):
	number = 0
	counter = len(digits) - 1
	for digit in digits:
		number += digit*(10**counter) 
		counter -= 1
	return number

print (to_number([1,2,3,0,2,3]))
print (to_number([9,9,9,9,9]))
