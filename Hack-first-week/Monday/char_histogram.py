def char_histogram(string):
	letters = list(set(string))
	histogram = {}
	for letter in string:
		histogram[letter] = string.count(letter)
	return histogram

print (char_histogram("Python!"))
print (char_histogram("AAAAaaa!!!"))