import string

def sed(pattern, repl, f1, f2):
	"""
	Copies the contents of one file into another file, but replaces the pattern string with the replacement string.
	pattern: the string to replace
	repl: the string to replace with
	f1: string; name of file to read, including extension.
	f2: string; name of file to write into, including extension. File will be created if it doesn't exist yet.
	"""
	# open f1 to read. If f1 doesn't exist, then print an error message and exit.
	try:
		fin = open(f1)
		s = fin.read()
		fin.close()

		s_new = s.replace(pattern, repl)

		fout = open(f2, "w")
		fout.write(s_new)
		fout.close()
	except:
		print("Input file does not exist")