# get the reverse complement of a DNA sequence... hey, Biopython has a method for that!
from Bio.Seq import Seq

my_file = open("rosalind_revc.txt", "r") #rosalind_dna.txt as placeholder
data = my_file.read()
my_file.close()

my_seq = Seq(data)

# Create the reverse complement
rev_comp = my_seq.reverse_complement()

print(rev_comp)