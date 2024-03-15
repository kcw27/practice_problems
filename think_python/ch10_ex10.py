def in_bisect(t, v):
	"""
	Performs an alphabetic bisection search for value v in list t.
	Precondition: t is assumed to be sorted.
	"""
	if len(t) <= 10: #10: # arbitrary "small-enough" list length for base case
		return v in t

	mid = len(t) // 2 # midpoint of list (keep in mind that it's 0-indexed)

	if t[mid] < v: # if the midpoint word comes before v alphabetically
		return in_bisect(t[mid+1:], v)
	elif t[mid] > v: # if the midpoint word comes after v alphabetically
		return in_bisect(t[:mid], v)
	else: # if the midpoint word happens to be v
		return True
