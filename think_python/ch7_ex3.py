import math

def estimate_pi():
	"""Estimates pi using Srinivasa Ramanujan's infinite series."""
	sum = 0
	k = 0

	while True:
		num = math.factorial(4*k) * (1103 + 26390*k)
		denom = math.factorial(k)**4 * 396**(4*k)
		term = num / denom
		sum += term

		if term < 1e-15:
			break
		k += 1

	one_over_pi = sum * math.sqrt(8)/9801
	pi = 1 / one_over_pi

	return pi

my_pi = estimate_pi()
print("My estimate of pi:", my_pi)
print("Difference between my estimate and math.pi:", abs(math.pi - my_pi))