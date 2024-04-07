import shelve
import ch12_ex2 as anagram_sets 

def store_anagrams(filename="words_anagrams"):
	"""
	Stores the anagram dictionary from chapter 12 exercise 2 in a "shelf".
	The user may assign a filename to the shelf.
	"""
	d = anagram_sets.anagrams() # Keys: strings of alphabetically-sorted characters. Values: lists of anagrams

	shelf = shelve.open(filename) # default flag is "c", which will create a new db if filename doesn't exist yet
	for chara_set in d:
		shelf[chara_set] = d[chara_set]
	shelf.close()

#store_anagrams()

def read_anagrams(word, filename="words_anagrams"):
	"""
	Searches for the given word in the anagram dictionary shelved at filename.
	Returns the list of anagrams of that word.
	"""
	try:
		shelf = shelve.open(filename, flag="r")
	except:
		print("Shelf at", filename, "does not exist.")
		return None

	key = "".join(sorted(word))
	try:
		t = shelf[key]
		if word in t: # this conditional was added in case the user types a sequence that isn't a real word
			t.remove(word)
		shelf.close()
		return t
	except KeyError: # if the word doesn't exist in the word list...
		print(word, "not found.")
		shelf.close()
		return [] # then it has no anagrams

shelf = shelve.open("words_anagrams")
print(shelf["aeffrsz"])
print(read_anagrams("astringe"))
print(read_anagrams("gratines")) # not a real word, but it's an anagram of a key in the anagrams dictionary
print(read_anagrams("wiggler", filename = "wordle")) # this file doesn't exist
print(read_anagrams("apartment")) # for some reason, this word isn't in the original word list at all
print(read_anagrams("frog")) # it's in the original word list, but has no anagrams.