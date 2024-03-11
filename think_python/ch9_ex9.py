def find_reverses():
	"""
	Determines the current age of the author of the Car Talk Puzzler, as specified by the exercise prompt.
	"""
	d = {}

	for a in range(10):
		for b in range(10):
			n1 = str(a) + str(b)
			n2 = str(b) + str(a)
			offset = abs(int(n1) - int(n2))

			if offset in d:
				if [b,a] not in d[offset]: # prevents duplicates so that the reverse count will be accurate
					d[offset].append([a,b])
			else:
				d[offset] = [[a,b]]

	real_offset = 0 # initalize as int, not list; rely on assumption that there's only one solution

	for offset in d:
		if len(d[offset]) == 8: # ages of author and mother are reverses 8 times in total
			real_offset = offset
			break

	digits_list = d[real_offset]
	print("There is a difference in age of", real_offset, "years between mother and child.")
	print("Here's the list of digits that result in the two ages being reverses of each other:", digits_list)

	current = digits_list[5] # the author mentions that this is the 6th time that their ages are reverses

	age1 = int(str(current[0]) + str(current[1]))
	age2 = int(str(current[1]) + str(current[0]))
	print("The current ages are", age1, "and", age2)

	return min(age1, age2) # return the author's age

print("The author's age is", find_reverses())