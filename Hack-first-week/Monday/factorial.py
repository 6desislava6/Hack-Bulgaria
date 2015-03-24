def factorial(n):
	result = 1
	if n<2:
		return 1;
	elif n<0: 
		return "Not correct!"
	else:
		for x in range(2,n+1):
			result *= x
		return result


print (factorial(1))
print (factorial(0))
print (factorial(5))