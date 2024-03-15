import ch10_ex10 as ex10

def reverse_pairs():
	"""
	Finds all reverse pairs in words_moby.txt.
	Two words are a reverse pair if spelling one word backwards makes the other.
	"""
	fin = open("words_moby.txt")
	t = [] # will be the words list
	for line in fin:
		word = line.strip()
		t.append(word)
	fin.close()

	pairs = [] # list of reverse pairs
	for w in t:
		if ex10.in_bisect(t,w[::-1]):
			if [w[::-1], w] not in pairs:
				pairs.append([w, w[::-1]])

	return pairs

print(reverse_pairs())
