import string

def file_to_words(filename):
	"""
	Reads a book in plaintext format.
	Skips the header and footer. Converts each line into a list of lowercase words stripped of punctuation and whitespace.
	Counts the total number of words in the book, and the frequencies of each word.
	Prints words that do not appear in the Moby Project word list.

	filename is a string that specifies the path to the file for this function to process.
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
	d = {} # dictionary of word frequencies

	for i in range(start, end): # for each line in words
		words_in_line = []
		stripped = words[i].translate(my_table) # all words in the line to lowercase, and punctuation removed
		for word in stripped.split(): # the split removes any whitespace, including spaces translated from "-"
			word = word.strip("'") # to remove any leading/trailing apostrophes, since these aren't contractions
			words_in_line.append(word)
			d[word] = d.get(word, 0) + 1 # add to freq dictionary
		words_strip.append(words_in_line)

	book_length = sum([len(t) for t in words_strip])
	print("This book is", book_length, "words long.")

	print(len(d), "unique words are used in the book.\n")

	print("Top 20 words and their frequencies:")
	word_sort = sorted(d, key = lambda x: d[x], reverse = True) # word list sorted in descending order by word frequencies
	for top_word in word_sort[:20]:
		print(top_word + ": " + str(d[top_word]) + " (" + str(100*d[top_word]/book_length) + "%)")

	print("\nThe full dictionary of word frequencies is returned by this function.")

	fin2 = open("words_moby.txt") # English word list
	english = fin2.read().split()
	fin2.close()

	print("These words appeared in the book but not in the Moby Project word list:")
	not_in = [w for w in d if w not in english]
	print(not_in)

	return d

file_to_words("words_anne.txt")