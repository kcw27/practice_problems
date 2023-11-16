# Returns the Hamming distance between two strings

my_file = open('rosalind_hamm.txt', 'r')
data = my_file.read()
my_file.close()

seq_list = data.split('\n') # should have two DNA strings in it

def hamming(s, t):
	"""
	Returns the Hamming distance (number of corresponding symbols that differ) between DNA strings s and t.
	s and t are assumed to be of equal length.
	"""

	dist = 0

	for i in range(len(s)):
		if s[i] != t[i]:
			dist += 1

	return dist

print(hamming(seq_list[0], seq_list[1]))

# According to the corresponding solutions forum on Rosalind, a more efficient approach is sum(a != b for a, b in itertools.izip(s1, s2))