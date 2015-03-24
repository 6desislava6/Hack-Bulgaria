def count_words(arr):
	unique_words = set(arr)
	dict_of_words_occur = {}
	for word in unique_words:
		dict_of_words_occur[word] = arr.count(word)
	return dict_of_words_occur
print(count_words(["apple", "banana", "apple", "pie"]))

def count_words2(arr):
	dict_of_words_occur = {}
	for word in arr:
		if word in dict_of_words_occur:
			dict_of_words_occur[word] += 1
		else:
			dict_of_words_occur = 1
	return dict_of_words_occur


print(count_words(["apple", "banana", "apple", "pie"]))
print(count_words2(["apple", "banana", "apple", "pie"]))