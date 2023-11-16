# Given a string s, print two slices of the string using the indices specified in a txt file.

my_file = open('rosalind_ini3.txt', 'r')
data = my_file.read()
data_into_list = data.split("\n")
my_file.close()

my_string = data_into_list[0]

list_of_indices = data_into_list[1].split(' ') # all the elements are currently str, not int
a, b, c, d = [int(i) for i in list_of_indices]

print(my_string[a:b+1], my_string[c:d+1])