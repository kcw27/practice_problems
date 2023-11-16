# Counts the occurrences of each base in a string of nucleotides

my_file = open("rosalind_dna.txt", "r")
data = my_file.read() # this is a string
my_file.close()

# Could use an if statement to make it only count the A's, C's, G's, and T's to the dictionary
def histogram(s):
	d = dict()
	for chara in s:
		d[chara] = d.get(chara, 0) + 1
	return d

nuc_counts = histogram(data)

print(nuc_counts.get('A', 0), nuc_counts.get('C', 0), nuc_counts.get('G', 0), nuc_counts.get('T', 0))

# Here's another implementation using BioPython
# Data structure "Seq": like a string, but with methods that are useful for biology, like translate() and reverse_complement()
# In this case, I used the built-in Python method .count().

from Bio.Seq import Seq

my_file2 = open("rosalind_dna.txt", "r")
data2 = my_file2.read()
my_file2.close()

my_seq = Seq(data)

print(my_seq.count("A"), my_seq.count("C"), my_seq.count("G"), my_seq.count("T"))