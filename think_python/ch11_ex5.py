word_file = open('wordlist.txt', 'r') # Words from https://www.randomlists.com/random-words?dup=false&qty=500; added "melon" and "cubed" at the beginning to ensure that there would be at least one rotate pair
word_data = word_file.read()
word_list = word_data.split('\n')

# my wordlist has everything in lowercase already, but I want to make absolutely sure that everything is always in lowercase
for i in range(len(word_list)):
	word_list[i] = word_list[i].lower()


# I'll be using ord to compare characters. ord('a') is 97, and ord('z') is 122.

def rotate_letter(letter1, letter2, diff): # 
	"""
	Checks whether letter2 is equivalent to letter1 rotated by diff amount.
	"""

	rotated_letter1 = ord(letter1) + diff # diff can either be positive or negative

	if rotated_letter1 < 97: # rotated index below 'a'
		rotated_letter1 += 26 # wrap around to end of alphabet
	elif rotated_letter1 > 122: # rotated index above 'z'
		rotated_letter1 -= 26 # wrap around to beginning of alphabet

	# now compare the rotated index of letter1 to word2's corresponding letter, letter2
	return rotated_letter1 == ord(letter2) # True if the letters are a rotate pair, False otherwise

# debug for rotate_letter()
#print(rotate_letter('a', 'c', 2)) # should be True
#print(rotate_letter('a', 'c', 3)) # should be False
#print(rotate_letter('a', 'y', -2)) # should be True
#print(rotate_letter('w', 'b', 5)) # should be True

rotate_memo = dict()

def rotate_word(word1, word2):
	"""
	Checks whether word1 and word2 are a rotate pair.
	"""

	if (word1, word2) in rotate_memo: # as stated below, order of comparison won't matter
		print(word1, "and", word2, "have been compared already.")
		return rotate_memo[(word1, word2)]

	if len(word1) != len(word2):
		rotate_memo[(word1, word2)] = rotate_memo[(word2, word1)] = False # two keys so that order of comparison doesn't matter
		return False

	# otherwise, do compare the two words
	diff = ord(word2[0]) - ord(word1[0]) # if the words are a rotate pair, the diff in position for each pair of letters will be the same
	
	for i in range(len(word1))[1:]: # would be redundant to run rotate_letter on the first pair of letters
		if rotate_letter(word1[i], word2[i], diff) == False:
			rotate_memo[(word1, word2)] = rotate_memo[(word2, word1)] = False
			return False
	
	rotate_memo[(word1, word2)] = rotate_memo[(word2, word1)] = True

	return True

# debug for rotate_word(). The first two lines put some comparisons in the dictionary so that I can test that the memoization works.
print("melon and cube are a rotate pair:", rotate_word('melon', 'cubed')) # rotate pair
print("tie and magical are a rotate pair:", rotate_word('tie', 'magical')) # both appear in wordslist, but "magical" appears before "tie" in wordslist
#print(rotate_word('elon', 'musk'))
#print(rotate_word('rat', 'cheese'))
#print(rotate_memo)
print()


def find_rotate_pairs(wordlist):
	"""
	Returns any rotate pairs within wordlist.
	"""

	rotate_pairs_list = []

	for i in range(len(wordlist)):
		for j in range(len(wordlist))[i+1:]: # would be redundant to compare a word against itself or anything that came before it
			if rotate_word(wordlist[i], wordlist[j]) == True:
				rotate_pairs_list.append((wordlist[i], wordlist[j]))
	if rotate_pairs_list == []:
		print('No rotate pairs were found.')
	return rotate_pairs_list
		
# debug for find_rotate_pairs()
#print(find_rotate_pairs(word_list[:10])) # start by testing just a small subset that does contain a known pair
#print(find_rotate_pairs(word_list[1:10])) # what if there are no pairs? Then it just returns an empty list.


print("Rotate pairs found:", find_rotate_pairs(word_list)) # it seems like there really were no rotate pairs other than the one I intentionally included

# I want to check that my dictionary has the right number of comparisons (i.e. that we checked all possible word pairs)
comparisons = 0
for i in reversed(range(502)): # there are 502 words in my list. The first word compares against 501 others (the highest number that the range gives us is 501), the second word is compared against 500 others, so on and so forth.
	comparisons += i

print('All possible comparisons have been made among this list of words:', len(rotate_memo) == comparisons*2) # multiply comparisons by 2 because two dictionary keys were created for each comparison: (word1, word2) and (word2, word1)
# this comparison doesn't work if the dictionary also contains comparisons that didn't come from rotate_memo, e.g. if I uncomment print(rotate_word('elon', 'musk')) then there are two extra comparisons

print(len(rotate_memo), 'comparisons were made')
