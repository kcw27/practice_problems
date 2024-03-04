def eval_loop():
	"""
	Iteratively evaluates mathematical expressions entered by the user. Type "done" to exit.
	Returns the value of the last expression evaluated.
	"""
	y = "" # initialize y in case "done" is the first thing typed

	while True:
		x = input("Input: ")
		if x == "done":
			break
		y = eval(x)
		print(y)

	return y # returns the value of the last expression evaluated

print("Value of last expression evaluated:", eval_loop())