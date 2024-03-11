def is_palindrome(word):
	return word == word[::-1]

def odometer():
	"""
	Finds the solution to the Car Talk Puzzler specified by the exercise prompt.
	"""
	for i in range(100000, 1000000):
		if is_palindrome(str(i)[2:]):
			if is_palindrome(str(i+1)[1:]):
				if is_palindrome(str(i+2)[1:5]):
					if is_palindrome(str(i+3)):
						return i

print(odometer())