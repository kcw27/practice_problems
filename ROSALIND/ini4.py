# Given two positive integers, return the sum of all odd integers between them, inclusively.

my_file = open('rosalind_ini4.txt', 'r')
data = my_file.read()
my_file.close()

data_into_list = data.split(" ")
a, b = [int(num) for num in data_into_list]

num = 0
for i in range(a, b+1):
	if i%2 == 1:
		num += i
print(num)