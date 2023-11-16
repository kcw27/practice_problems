# Given some DNA strings in FASTA format, return the ID of the string with the highest GC-content, followed by its GC-content.
import Bio.SeqUtils

my_file = open("rosalind_gc.txt", "r")
data = my_file.read()

data_into_list = data.split(">")

data_into_list = data_into_list[1:] # to get rid of the empty first element

my_dict = {}

for id_seq_pair in data_into_list:
	seq_ID = id_seq_pair[:13] # the ID is the first 13 digits of each string in data_into_list
	seq_name = id_seq_pair[13:]
	seq_name = seq_name.replace("\n", "") #then deal with the newlines
	my_dict[seq_ID] = seq_name

GC_content = {}
for key in my_dict:
	GC_content[key] = Bio.SeqUtils.gc_fraction(my_dict[key]) * 100 # convert from decimal to percent

max_key = max(GC_content, key = GC_content.get)
print(max_key)
max_value = max(GC_content.values())
print(max_value)
