def count_vowels(str):
	str = str.lower()
	vowels = ['a','e','i','o','u','y']
	count = 0
	for letter in str:
		if letter in vowels:
			count += 1
	return count

print (count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))