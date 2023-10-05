my_file = open("words.txt", "r")
words = my_file.read() # string


def remove_punct(s):
	"""
	Strips punctuation from string s.
	"""

	punctuation = {".":"", ",":"", "!":"", "?":""} # not getting rid of ' because it's part of some words 

	for i, j in punctuation.items():
		s = s.replace(i, j)
	return s


def add_to_dict(text):
	"""
	Returns a dictionary in which keys are words that appear in text, and each value is how many times the word appears in text.
	text: a list of strings
	"""
	d = dict()
	for w in text:
		d[w] = d.get(w, 0)+1
	return d

def check_dict(word, dict):
	"""
	Prints whether a word is present in a given dictionary or not.
	"""
	
	if word in dict:
		print('"' + word + '"', 'is present in the text.')
	else:
		print('"' + word + '"', 'is not present in the text.')

words = remove_punct(words)
# words = words.lower() # can use this if you don't want the word counts to be case-sensitive
	
words_list = words.split(' ')
words_freqs = add_to_dict(words_list)


check_dict('Horatio', words_freqs)
check_dict('Shakespeare', words_freqs)