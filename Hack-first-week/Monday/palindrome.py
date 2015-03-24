import math
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