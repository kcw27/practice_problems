def right_justify(s):
	"""
	Prints string s with leading spaces, such that the last letter of s is in column 70.
	"""
	spaces = 70 - len(s)
	justified = ' ' * spaces + s
	print(justified)

right_justify('python')

right_justify('According to all known laws of aviation')



