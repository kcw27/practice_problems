from random import randint

def has_duplicates(t):
	"""
	Returns True if list t has any element that appears more than once.
	"""
	d = []
	for e in t:
		if e in d:
			return True
		d.append(e)
	return False

def birthday():
	"""
	For a class of 23 students, estimates the chance that two students have the same birthday. 
	Randomly generates samples of size 23.
	"""
	classes = []
	for i in range(1000): # arbitrarily using 1000 replicates (1000 classes of 23 students)
		bdays = [randint(1,365) for j in range(23)] # randomly generates bdays for 23 students, ignoring leap days
		classes.append(has_duplicates(bdays)) 
	return sum(classes) / len(classes) # exploit the int values of True (1) and False (0) to calculate proportion of True values returned by has_duplicate

print(birthday()) # there seems to be about a 50% chance that two students in a class of 23 have the same birthday