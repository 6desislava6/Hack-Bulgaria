from palindrome import palindrome
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
