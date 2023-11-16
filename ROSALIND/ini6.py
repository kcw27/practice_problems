# Print the number of occurrences of each word in a string

my_file = open('rosalind_ini6.txt', 'r')
data = my_file.read()
my_file.close()

word_list = data.replace('\n', '').split(' ')

word_count = dict()

for word in word_list:
	word_count[word] = word_count.get(word, 0) + 1

for word in word_count:
	print(word, word_count[word])
