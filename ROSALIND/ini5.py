# Print all even-numbered lines from the file

my_file = open('rosalind_ini5.txt', 'r')
data = my_file.read()
my_file.close()

data_into_list = data.split('\n')

for i in range(len(data_into_list)):
	if i % 2 == 1: # the range is 0-indexed, but we index lines starting from 1
		print(data_into_list[i])
