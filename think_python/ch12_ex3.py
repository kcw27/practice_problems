from ch12_ex2 import anagrams

def meta(w1, w2):
	"""
	Helper function for metathesis. Encapsulated as its own function for legibility.
	w1 and w2 are strings of the same length.
	"""
	i=0
	while i < len(w1)-1:
		j = i+1
		while j < len(w1):
			temp = w1[:i] + w1[j] + w1[i+1:j] + w1[i] + w1[j+1:] # string with letters at indices i and j swapped
			if temp == w2:
				return True
			j += 1
		i += 1
	return False

print(meta("converse", "conserve"))
print(meta("abcde", "aebcd"))

def metathesis():
	"""
	Finds metathesis pairs in words_moby.txt.
	Metathesis: you can transform one word into the other by swapping two letters.
	"""
	a = tuple(anagrams().values()) # metathesis pairs are necesssarily anagrams
	meta_pairs = []

	for word_set in a: # each word set is at least two words long
		for i in range(len(word_set)-1):
			j = i+1 # the loop is set up this way so that there are no repeat comparisons
			while j < len(word_set):
				if meta(word_set[i], word_set[j]):
					meta_pairs.append([word_set[i], word_set[j]])
				j += 1

	return meta_pairs

print(metathesis())