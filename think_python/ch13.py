# Exercises 1 and 2
import string

def analyze_book(filename):
	"""
	Reads a book in plaintext format.
	Skips the header and footer. Converts each line into a list of lowercase words stripped of punctuation and whitespace.
	Returns a histogram of word frequencies.

	filename: string that specifies the filepath to a book.
	"""
	fin = open(filename)
	words = fin.read().split("\n") # list of lines in the file
	fin.close()

	# initialize start and end indices so that if the file doesn't contain headers or footers, the code will still work
	start = 0
	end = len(words)

	for i in range(len(words)):
		if "START OF THE PROJECT GUTENBERG EBOOK" in words[i]:
			start = i + 1 # have to add 1 so that the selection won't include this line
	for j in range(len(words)-1, 0, -1): # count backwards from the end to save time
		if "END OF THE PROJECT GUTENBERG EBOOK" in words[j]:
			end = j # not necessary to subtract 1 because the upper bound of range is non-inclusive

	# setting up a mapping table for use with translate
	uppercase = "".join([chr(k) for k in range(65,65+26)] + ["-"])
	lowercase = "".join([chr(k) for k in range(97,97+26)] + [" "])
	punct_t = list(string.punctuation)
	punct_t.remove("-") # "-" separates words so it's replaced with a space, rather than removed entirely
	punct_t.remove("'") # "'" is used in contractions, so it's part of some words
	punct = "".join(punct_t)
	my_table = str.maketrans(uppercase, lowercase, punct) # mapping table: make lowercase, remove specified punctuation

	words_strip = [] # will be a list of lists; each sublist contains one line of words
	hist = {} # histogram of word frequencies

	for i in range(start, end): # for each line in words
		words_in_line = []
		stripped = words[i].translate(my_table) # all words in the line to lowercase, and punctuation removed
		for word in stripped.split(): # the split removes any whitespace, including spaces translated from "-"
			word = word.strip("'") # to remove any leading/trailing apostrophes, since these aren't contractions
			words_in_line.append(word)
			hist[word] = hist.get(word, 0) + 1 # add to freq dictionary
		words_strip.append(words_in_line)

	return hist

def vocab_info(hist):
	"""
	Prints the total number of words and number of unique words in a book.
	hist: a word histogram generated using analyze_book.
	"""
	book_length = sum(hist.values())
	print("This book is", book_length, "words long.")
	print(len(hist), "unique words are used in the book.\n")

anne = analyze_book("words_anne.txt")
vocab_info(anne)

# Exercise 3
def top_words(hist, length=20):
	"""
	Prints the most frequently used words in a book.
	The user can determine how many words to display using the len parameter.
	hist: a word histogram generated using analyze_book.
	"""
	print("Top", length, "words and their frequencies:")
	word_sort = sorted(hist, key = lambda x: hist[x], reverse = True) # word list sorted in descending order by freqs
	book_length = sum(hist.values())

	for top_word in word_sort[:length]:
		print(top_word, "\t", hist[top_word], "\t(", 100*hist[top_word]/book_length, "%)", sep="")
	print()

top_words(anne)

# Exercise 4
def not_in(hist, wordlist, preview=100):
	"""
	Prints and returns words that do not appear in the input word list.
	hist: a word histogram generated using analyze_book.
	wordlist: a string that specifies the path to the word list for comparison
	preview: how many words to print in the print preview. The entire list is returned by the function, however.
	If preview<0, it prints the whole list.
	"""
	fin = open(wordlist)
	words = fin.read().split()
	fin.close()

	print("These are some words that appeared in the book but not in the given word list:")
	book_only = [w for w in hist if w not in words]
	# exercise 6 is essentially the same but with a set comprehension instead of list comprehension
	# the only difference in exercise 6's solution is that curly brackets are used instead of square brackets

	if preview >= 0:
		to_print = book_only[:preview]
	else:
		to_print = book_only

	for word in to_print:
		print(word, end=" ")
	print("\n\n")

	return book_only

not_in(anne, "words_moby.txt")

# Exercises 5 and 7
import random

def cumsum(t):
	"""
	Takes t, which is a list of numbers, and returns a list of cumulative sums.
	"""
	v = []
	for i in range(len(t)):
		v.append(sum(t[:i+1])) # sum of the first i elements of the list
	return v

def bisect_word(r, cumufreqs, vocab):
	"""
	Auxiliary function for hist_choice. Performs a bisect search to see where r should be inserted in cumufreqs,
	and thus which word from vocab corresponds to r.
	r: random int in [1, n]
	cumufreqs: (full or partial) list of cumulative frequencies ranging from 1 to n.
	vocab: (full or partial) list of words. Indices match with cumufreqs's.
	"""
	mid = len(cumufreqs) // 2

	if mid == 0 or (r <= cumufreqs[mid] and r > cumufreqs[mid-1]): 
	# if cumufreqs is only one element long, can't (and doesn't need to) compare two elements from cumufreqs
		#print("1:", r, cumufreqs, vocab)
		return vocab[mid]
	elif r <= cumufreqs[mid-1]: # if r is even smaller than, or equal to, cumufreqs[mid-1]
		#print("2:", r, cumufreqs, vocab)
		return bisect_word(r, cumufreqs[:mid], vocab[:mid]) # searches up to mid-1, non-inclusive 
	else: # if r is even bigger than cumufreqs[mid]
		#print("3:", r, cumufreqs, vocab)
		return bisect_word(r, cumufreqs[mid+1:], vocab[mid+1:])

def get_hist_info(hist):
	"""
	Helper function for hist_choice and hist_multichoice.
	hist: a word histogram generated using analyze_book.
	"""
	vocab = list(hist.keys())
	freqs = list(hist.values())
	cumufreqs = cumsum(freqs)
	n = cumufreqs[-1] # last element of cumufreqs is the total number of words in the histogram

	return n, cumufreqs, vocab

def hist_choice(hist):
	"""
	Chooses a random word from a book according to word frequencies.
	hist: a word histogram generated using analyze_book.
	"""
	n, cumufreqs, vocab = get_hist_info(hist)

	r = random.randint(1, n) # picks from 1 to n inclusive
	randword = bisect_word(r, cumufreqs, vocab)

	return randword

def hist_multichoice(hist, length=100):
	"""
	Generates multiple words according to word frequencies from the book, and prints additional info.
	"""
	n, cumufreqs, vocab = get_hist_info(hist)

	print("Here are some random words from the input book:")
	randwords = []
	for i in range(length):
		r = random.randint(1, n) # picks from 1 to n inclusive
		randword = bisect_word(r, cumufreqs, vocab)
		print(randword, end=" ")
		randwords.append(randword)

	randhist = {}
	for word in randwords:
		randhist[word] = randhist.get(word, 0) + 1

	print("\nDuplicates among randomly-generated words and their frequencies:", 
		{k:randhist[k] for k in randhist if randhist[k] > 1})
	print()

print("One randomly-selected word:", hist_choice(anne), "\n")
hist_multichoice(anne)

# Exercise 8
def markov(book, prefix=2):
	"""
	Uses Markov analysis based on the input word file.
	Leaves punctuation on words. 
	book: filepath to a .txt file containing a book.
	prefix: prefix length for Markov analysis. Words are assumed to be separated by whitespace.
	"""
	# since we want the punctuation here, this includes a modified version of analyze_book.
	fin = open(book)
	words = fin.read().split("\n") # list of lines in the file
	fin.close()

	# initialize start and end indices so that if the file doesn't contain headers or footers, the code will still work
	start = 0
	end = len(words)

	for i in range(len(words)):
		if "START OF THE PROJECT GUTENBERG EBOOK" in words[i]:
			start = i
	for j in range(len(words)-1, 0, -1): # count backwards from the end to save time
		if "END OF THE PROJECT GUTENBERG EBOOK" in words[j]:
			end = j

	words_cropped = " ".join(words[start+1:end])

	words_list = words_cropped.split()

	d = {} # prefix histogram in the format of (p1, p2, ...) : {s1:n1, s2:n2, ...}

	max = len(words_list)-prefix-1 # range goes up to this value so there's enough room for the prefix and a suffix word
	for i in range(0, max):
		key = tuple(words_list[i:i+prefix])
		suffix = words_list[i+prefix] # the word immediately following the prefix

		if key in d:
			d[key][suffix] = d[key].get(suffix, 0) + 1
		else:
			d[key] = {suffix:1} # initializes a dictionary corresponding to that key; first entry is that suffix

	return d

def print_markov(d, length=100):
	"""
	Prints random text based on Markov analysis.
	d: Markov analysis dictionary
	length: length of text to randomly generate.
	"""
	prefixes = list(d.keys())
	first = random.choice(prefixes) # initialize by randomly selecting from all prefixes available
	rand_list = [w for w in first] # get the words out of that tuple
	prefix = len(first) # the prefix length that the dictionary was built with

	for i in range(length-prefix):
		preceding = tuple(rand_list[-prefix:]) # gets the last few words from randlist (depends on prefix length)
		suff = hist_choice(d[preceding]) # selects from the possible suffixes for the prefix, based on frequency
		rand_list.append(suff)
		
	rand_text = " ".join(rand_list)
	print(rand_text)
	

markov_anne = markov("words_anne.txt")
print("Some text generated using Markov analysis:")
print_markov(markov_anne)
print()
#print({k:markov_anne[k] for k in markov_anne if len(markov_anne[k]) > 1})

# Exercise 9
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def zipf(hist):
	"""
	Tests Zipf's Law on text input, and plots the results.

	Zipf's Law: in a natural language, the relationship between a word's rank and frequency is f=cr^(-s)
		f: frequency of a word
		r: rank of a word (most common word has rank 1, second most common has rank 2, etc.)
		c and s are parameters that depend on the language and the text.

	hist: a word histogram generated using analyze_book.
	"""
	word_sort = sorted(hist, key = lambda x: hist[x], reverse = True) # word list sorted in descending order by freqs

	# the rank (r) of a word is i+1, where i is its index in word_sort
	ranks = [i+1 for i in range(len(word_sort))]
	# get the frequency (f) of a word by looking it up in hist
	freqs = [hist[k] for k in word_sort]

	# Zipf's Law is f=cr^(-s), which means logf = logc - s*logr
	# so with logf plotted on the y axis and logr on the x axis, you get the slope -s and y-intercept logc.
	logf = [math.log(f) for f in freqs]
	logr = [math.log(r) for r in ranks]

	# plotting the data
	fig, ax = plt.subplots()
	ax.plot(logr, logf)

	slope, intercept = np.polyfit(logr, logf, 1) # fits a line to the plot with these coordinates
	print("Slope:", slope, "\nIntercept:", intercept)
	ax.axline((0, intercept), slope=slope, color="lightcoral", label="linear fit")
	plt.show() # for my computer, this is necessary for getting the plot to show

zipf(anne)
# Based on how the linear fit compares to the plot of actual data, and a quick glance at freqs, it seems like the data is heavily weighted toward words that appear only once or a few times. This means that the intercept of the linear fit is much higher than the observed intercept.
