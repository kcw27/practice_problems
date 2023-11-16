# If we begin with 1 rabbit pair, and during each generation, every pair of reproduction-age rabbits (1+ months old) produces a litter of k rabbit pairs, how many rabbit pairs will be present after n months? (Rabbits are immortal.)

my_file = open("rosalind_fib.txt", "r")
data = my_file.read()
my_file.close()

data_into_list = data.replace('\n', '').split(' ') #if there's a newline character at the end, this gets rid of it entirely
		
n, k = [int(i) for i in data_into_list] # n is number of months, k is litters produced per reproduction-age rabbit

known = {0:0, 1:1} # for memoization

def reproduce(months, litters):
	"""Like a Fibonacci function, but generalized to allow the user to set how many litters are produced per month by each reproductive-age pair."""
	if months in known:
		return known[months]
	
	total = reproduce(months-1, litters) + reproduce(months-2, litters)*litters # this is the line where it differs from a typical Fibonacci function
	known[months] = total
	return total

print(reproduce(n, k))