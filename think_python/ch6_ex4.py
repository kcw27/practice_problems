def is_power(a, b):
	"""
	For integers a and b, returns true if a is a power of b.
	"""
	if a == b: # base case
		return True
	if a%b == 0:
		return is_power(a/b, b)
	return False

# returns True
print(is_power(1,1))
print(is_power(8,2))
print(is_power(27,3))
print(is_power(2048,2))
print(is_power(9,-3))

#returns False
print(is_power(8,4))
print(is_power(8,3))
print(is_power(27,-3))