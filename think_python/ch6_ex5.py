def gcd(a, b):
	"""
	Given integers a and b, returns their greatest common divisor
	(the largest number that divides them both with no remainder).
	"""
	if b==0:
		return a

	larger = max(a, b)
	smaller = min(a, b)
	r = larger%smaller # remainder

	return gcd(smaller, r) # if a%b=r, then gcd(a,b) == gcd(b,r)

print(gcd(26, 6))
print(gcd(6, 26))
print(gcd(70, 28))
print(gcd(5, 5))