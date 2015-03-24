def count_consonants(str):
	str = str.lower()
	consonantsAll = 'bcdfghjklmnpqrstvwxz'
	consonants = [x for x in consonantsAll]
	count = 0
	for letter in str:
		if letter in consonants:
			count += 1
	return count
print (count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print (count_consonants("A nice day to code!"))

