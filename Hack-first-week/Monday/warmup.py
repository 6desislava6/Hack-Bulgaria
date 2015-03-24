import math
#No if...

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

def fact_digits(number):
	digits = []
	sum = 0
	while (number > 0):
		digit = number % 10
		digits.append(digit)
		number = number//10
	for digit in digits:
		sum += factorial(digit)
	return sum

print (fact_digits(111))
print (fact_digits(999))

def palindrome(obj):
	string = str(obj)
	length =len(string)
	is_palindrome = True
	for n in range(0, math.floor(length/2)):
		if string[n] != string[length-n-1]:
			is_palindrome = False
	return is_palindrome

print (palindrome("kapak"))
print (palindrome("baba"))
print (palindrome(121))

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

def to_number(digits):
	number = 0
	counter = len(digits) - 1
	for digit in digits:
		number += digit*(10**counter) 
		counter -= 1
	return number

print (to_number([1,2,3,0,2,3]))
print (to_number([9,9,9,9,9]))

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
		return number(result)

print (fib_number(10))

def count_vowels(str):
	str.lower()
	vowels = ['a','e','i','o','u','y']
	count = 0
	for letter in str:
		if letter in vowels:
			count += 1
	return count

print (count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

def count_consonants(str):
	str.lower()
	vowels = ['bcdfghijklmnpqrstvwxz']
	count = 0
	for letter in str:
		if letter not in vowels:
			count += 1
	return count


print (count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

def char_histogram(string):
	letters = list(set(string))
	histogram = {}
	for letter in string:
		histogram[letter] = string.count(letter)
	return histogram

print (char_histogram("Python!"))
print (char_histogram("AAAAaaa!!!"))

def palindrome_score(number):
	if palindrome(number):
		return 1
	else:
		nums = []
		for x in str(number):
			nums.append(x)
		nums.reverse()
		str_num = ""
		for x in nums:
			str_num += x
		num = int(str_num)
		return 1 + palindrome_score(number + num)

print (palindrome_score(121)) 
print (palindrome_score(48)) 


def is_increasing(seq):
	is_incresing = True
	for i in range(0,len(seq)-1):
		if seq[i] >= seq[i+1]:
			is_incresing = False
			break
	return is_incresing

print(is_increasing([1,2,3,4,5]))
print (is_increasing([5,6,-10]))


def is_decreasing(seq):
	is_decreasing = True
	for i in range(0,len(seq)-1):
		if seq[i] <= seq[i+1]:
			is_decreasing = False
			break
	return is_decreasing

print(is_decreasing([5,4,3,2,1]))
print (is_decreasing([1,1,1,1]))

def hack_number (number):
	binary = bin_my(number)
	is_palindrome = palindrome (binary)
	count = binary.count('1')
	is_hack = (count % 2 == 1 and is_palindrome)
	return is_hack

def bin_my(i):
	if i == 0:
		return "0"
	s = ''
	while i:
		if i & 1 == 1:
			s = "1" + s
		else:
			s = "0" + s
		i >>= 1
	return s

def next_hack(n):
	number = n + 1
	while True:
		if hack_number(number):
			return number
			break
		number += 1

print (next_hack(8031))
