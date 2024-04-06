def anagrams():
	"""
	Reads words_moby.txt and prints all sets of words that are anagrams.
	"""
	d = {} # dictionary in the format of character set (tuple) : list of words using that character set
	fin = open("words_moby.txt")

	for line in fin:
		word = line.strip()
		charas = "".join(sorted(list(word))) # string of the word's letters in alphabetical order

		if charas in d:
			d[charas].append(word)
		else:
			d[charas] = [word]
	fin.close()

	d_sorted = {k:d[k] for k in sorted(d, key = lambda k: len(d[k]), reverse = True)} 
	d_final = {k: v for k, v in d_sorted.items() if len(d_sorted[k])>1} # removes words with unique character sets

	return d_final

def bingo():
	"""
	Finds the collection of 8 letters that forms the most possible bingos in Scrabble.
	"""
	a = anagrams() # note that anagrams already sorts by number of words in each anagram set, in descending order

	bingos = {k:a[k] for k in a if len(k)==8} # play all 7 tiles plus 1 tile on the board, hence the 8
	best = next(iter(bingos)) # the first value in bingos. Perhaps un-Pythonic, but anagrams was sorted and bingos kept the order.
	print("This set of 8 letters forms the most possible bingos in Scrabble:")
	print(best, bingos[best])

if __name__ == "__main__":
	print(anagrams())
	bingo()
