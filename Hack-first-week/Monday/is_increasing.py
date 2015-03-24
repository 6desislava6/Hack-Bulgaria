def is_increasing(seq):
	is_incresing = True
	for i in range(0,len(seq)-1):
		if seq[i] >= seq[i+1]:
			is_incresing = False
			break
	return is_incresing

print(is_increasing([1,2,3,4,5]))
print (is_increasing([5,6,-10]))