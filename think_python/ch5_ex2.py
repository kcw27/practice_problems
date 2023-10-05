def check_fermat(a, b, c, n):
	"""
	According to Fermat's Last Theorem, there should be no positive integers a, b, c, and n such that, if n > 2, a**n + b**n = c**n.
	a, b, c, and n must be positive integers, otherwise the program will refuse the input.
	"""

	# first check if the values entered are valid
	inputs = [a, b, c, n]

	for input in inputs:
		if type(input) != int: # this check isn't needed if you're collecting user inputs, because it won't accept non-int inputs.
			print("Please enter int arguments.")
			return
		if input < 0:
			print("Please enter positive integers.")
			return


	# now compute each side of the equation
	left = a**n + b**n
	right = c**n
	if n > 2:
		if left == right:
			print("Holy smokes, Fermat was wrong!", left, "==", right)
		else:
			print("No, that doesn't work.", left, "!=", right)
	else:
		print("You have selected n<=2, so Fermat's Last Theorem doesn't apply.")
		if left == right:
			print(left, "==", right)
		else:
			print(left, "!=", right)

def input_for_fermat():
	"""
	Takes user input for arguments of check_fermat().
	"""
	print("Please enter values for check_fermat() when prompted.\nThe function will check if a**n + b**n == c**n.")
	a = int(input("a="))
	b = int(input("b="))
	c = int(input("c="))
	n = int(input("n="))

	check_fermat(a, b, c, n)

input_for_fermat()