import ch10_ex10 as ex10

def interlock():
	"""
	Finds all pairs of words that interlock in words_moby.txt.
	For two words to interlock, taking alternating letters from each forms a new word.
	"""
	fin = open("words_moby.txt")
	t = [] # will be the words list
	for line in fin:
		word = line.strip()
		t.append(word)
	fin.close()

	pairs = {} # dictionary of interlock pairs
	for w in t:
		w1 = w[::2]
		w2 = w[1::2]
		if ex10.in_bisect(t,w1) and ex10.in_bisect(t,w2):
			pairs[w] = [w1,w2]

	return pairs

print(interlock())

def interlock_3():
	"""
	A version of interlock that checks for words that are three-way interlocked.
	"""
	fin = open("words_moby.txt")
	t = [] # will be the words list
	for line in fin:
		word = line.strip()
		t.append(word)
	fin.close()

	triplets = {} # dictionary of interlock triplets
	for w in t:
		w1 = w[::3]
		w2 = w[1::3]
		w3 = w[2::3]
		if ex10.in_bisect(t,w1) and ex10.in_bisect(t,w2) and ex10.in_bisect(t,w3):
			triplets[w] = [w1,w2,w3]

	return triplets

print(interlock_3())