def most_frequent(s):
	"""
	Prints the letters of string s in order of decreasing frequency.
	"""
	d = {} # to store letter frequencies
	alphabet = [chr(x + 97) for x in range(26)] # lowercase alphabet
	len_filtered = 0 # counter for letters

	for c in s.lower():
		if c in alphabet:
			d[c] = d.get(c, 0) + 1
			len_filtered += 1
	z = zip(d.keys(), d.values()) # letters, then frequencies

	z_sorted = sorted(z, key = lambda x: x[1], reverse = True) # sorts in descending order by letter frequencies

	print("Letter frequencies:")
	for k, v in z_sorted:
		print(k + ": " + str(v) + " (" + str(v/len_filtered*100) + "%)")

most_frequent("green eggs and ham?")

fin = open("words_moby.txt")
words = fin.read()
fin.close()
most_frequent(words)