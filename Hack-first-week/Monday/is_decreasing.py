def is_decreasing(seq):
	is_decreasing = True
	for i in range(0,len(seq)-1):
		if seq[i] <= seq[i+1]:
			is_decreasing = False
			break
	return is_decreasing

print(is_decreasing([5,4,3,2,1]))
print (is_decreasing([1,1,1,1]))