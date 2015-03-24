from palindrome import palindrome
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