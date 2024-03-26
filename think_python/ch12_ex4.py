# Program was drafted independently, then revised with assistance from the answer key https://github.com/AllenDowney/ThinkPython2/blob/master/code/reducible.py

families = {"":[""]} # memoization for word children; the child of an empty string is itself
fin = open("words_moby.txt")
words = fin.read().split()
words.extend(["", "a", "i"]) # added empty string (base case for reducible) and single-letter words
fin.close()

def children(word):
	"""
	Computes a list of words that can be formed by removing one letter from the given word.
	These are the "children" of the word.
	"""
	c = []

	for i in range(len(word)):
		candidate = word[:i] + word[i+1:] # excised word[i]
		if candidate in words and candidate not in c:
			c.append(candidate)
	return c

def reducible(word):
	"""
	If a word is reducible, returns a list of its reducible children. (Also memoizes it.)
	"""
	if word in families:
		return families[word]

	reducible_children = []
	for child in children(word):
		if reducible(child):
			reducible_children.append(child)

	families[word] = reducible_children
	return reducible_children

def reduce():
	"""
	Finds all words that can be reduced, and returns the five longest words.
	"""
	# "I" and "a" are the only single-letter words, so words are only eligible if they contain i or a.
	filtered = [w for w in words if ("i" in w or "a" in w)] 

	for word in filtered:
		reducible(word) # each word containing "a" and/or "i" is memoized in families

	can_reduce = [w for w in families if len(families[w]) > 0]


	# then you have to sort can_reduce to find the longest word
	can_reduce.sort(key=len, reverse=True)
	
	return can_reduce[:5]


longest = reduce()

def family_tree(word):
	"""
	For a word, prints the steps to reducing it down to a single-letter word. Prints all possible paths.
	"""
	print(word)
	if families[word] != ['']:
		for child in families[word]:
			family_tree(child)


print("Here are the five longest reducible words and the paths toward reducing them:")
for word in longest:
	children = families[word]
	for child in children:
		family_tree(child)
		print()