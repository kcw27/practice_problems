def init_search(word):
	"""
	Traverses word until it finds a pair of letters, at which point it uses search to check for consecutive pairs.
	"""
	word = word.lower()

	for i in range(len(word)-1):
		if word[i] == word[i+1]:
			if search(word[i+2:], count = 1) == True:
				return True
	return False

def search(substr, count):
	"""
	Checks for consecutive pairs in substr.
	substr: the substring of word
	count: how many (consecutive) pairs have been found so far
	"""
	if len(substr) >= 2:
		if substr[0] == substr[1]:
			return search(substr[2:], count + 1)
	
	return count >= 3

# should return True:
print(init_search("aABbcc"))
print(init_search("aabbccd"))
print(init_search("aabbdffgghh"))
print(init_search("      "))

# should return False:
print(init_search("aabbbccd"))
print(init_search("Mississippi"))
print(init_search(""))

def show_3consecpairs():
	"""
	Prints words with three consecutive pairs of letters.
	"""
	fin = open("words_moby.txt")

	for line in fin:
		word = line.strip()
		if init_search(word):
			print(word)

	fin.close()

show_3consecpairs()

