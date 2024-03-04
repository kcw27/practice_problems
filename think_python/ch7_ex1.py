import math
from tabulate import tabulate

def mysqrt(a):
	"""
	Returns an estimate (made using Newton's method) of the square root of non-negative float a.
	Implementation taken from the Think Python textbook.
	"""
	if a == 0:
		return 0.0 # to avoid dividing by 0

	epsilon = 0.0000001 # arbitrary small value
	x = a # initialize x as equal to a because it'll work no matter what a is

	while True:
		y = (x + a/x)/2
		if abs(x-y) < epsilon:
			break
		x = y

	return y

def test_square_root():
	"""
	Prints a table comparing the outputs of mysqrt(a) and the built-in function math.sqrt(a)
	for several values of a.
	"""
	foo = []

	for i in [i + 1.0 for i in range(9)]:
		sqrt = mysqrt(float(i))
		actual_sqrt = math.sqrt(float(i))
		diff = abs(sqrt - actual_sqrt)

		foo.append([i, sqrt, actual_sqrt, diff])

	nice_table = tabulate(foo, headers = ["a", "mysqrt(a)", "math.sqrt(a)", "diff"])
	print(nice_table) # seems to print floats without the decimal points if they're whole numbers

test_square_root()