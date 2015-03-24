def caesar_encrypt(word, number):
	encrypted = ""
	for i in range(0,len(word)):
		if ord(word[i]) >= 65 and ord(word[i]) <= 90:
			sum = (ord(word[i]) - 64 + number) % 26
			if sum == 0:
				sum = 26
			encrypted = encrypted + chr(sum + 64)

		if ord(word[i]) >= 97 and ord(word[i]) <= 122:
			sum = (ord(word[i]) - 96 + number) % 26
			if sum == 0:
				sum = 26
			encrypted = encrypted + chr(sum + 96)
	return encrypted

print (caesar_encrypt("abc", 1))
print (caesar_encrypt("ABC", 1))
print (caesar_encrypt("abc", 2))
print (caesar_encrypt("aaa", 7))
print (caesar_encrypt("xyz", 1))