# Print the probability that two randomly-selected organisms in the specified population will produce an offspring with the dominant allele

from itertools import repeat

my_file = open('rosalind_iprb.txt', 'r')
data = my_file.read()
my_file.close()

population = data.split(" ")
population = [int(x) for x in population] # list comprehension
k, m, n = population

def dominant(k, m, n):
	"""
	Returns the probability that two randomly selected mating organisms will product an individual with the dominant phenotype 
	(i.e. with at least one copy of the dominant allele). Assume any two organisms can mate.
	k individuals are homozygous dominant, m are heterozygous, and n are homozygous recessive.
	"""
	p = k + m + n # for concise code

	# probability of dominant phenotype for each pairing was calculated using Punnett squares
	branch1 = (k/p) * 1.00 # first partner is k; offspring has 100% chance of dominant phenotype regardless of second partner
	branch2 = (m/p) * (k*1.00 + (m-1)*0.75 + n*0.50)/(p-1) # first partner is m; sample second partner without replacement
	branch3 = (n/p) * (k*1.00 + m*0.50 + (n-1)*0.00)/(p-1) # first partner is n; sample second partner without replacement

	return branch1 + branch2 + branch3
	
print(dominant(k, m, n))