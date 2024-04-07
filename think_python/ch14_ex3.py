import os

dummypath = "C:\\Users\\achro\\OneDrive\\Desktop\\Python" # replace with your own filepath for testing

def all_paths_1(dirname, suffix):
	"""
	Searches a directory and all subdirectories. This version uses os.walk.
	Returns a list of complete paths for all files with the given suffix.
	directory: string of path. May be absolute or relative.
	"""
	paths = []

	try:
		w = tuple(os.walk(dirname)) # convert to tuple so indices can be used
		for i in range(len(w)):
			currdir = w[i][0]
			names = w[i][2]
			for name in names:
				joined = os.path.join(currdir, name)
				if os.path.isfile(joined) and joined.endswith(suffix):
					paths.append(joined)
	except FileNotFoundError:
		print(directory, "does not exist.")
	except NotADirectoryError:
		print(directory, "is not a directory.")

	return paths

paths1 = all_paths_1(dummypath, ".py")
#print("Output from directory search using os.walk:")
#for path in paths1:
	#print(path)

def all_paths_2(dirname, suffix):
	"""
	Searches a directory and all subdirectories. This version uses recursion.
	Returns a list of complete paths for all files with the given suffix.
	directory: string of path. May be absolute or relative.
	"""
	paths = []

	try:
		dirs = os.listdir(dirname)
		is_it_dir = [os.path.isdir(os.path.join(dirname, dir)) for dir in dirs] # os.path.isdir needs the full path 										# not just the name of the file/directory

		if sum(is_it_dir) == 0: # base case: if there are no subdirectories in the current directory
			return [os.path.join(dirname, x) for x in os.listdir(dirname) if x.endswith(suffix)]
		else:
			for x, y in zip(dirs, is_it_dir):
				if y == False and x.endswith(suffix): # if x is a file (not dir) ending with the suffix
					joined = os.path.join(dirname, x)
					paths.append(joined)
				if y == True: # so x is a directory
					for path in all_paths_2(os.path.join(dirname, x), suffix): # explore directory x
						joined = os.path.join(os.getcwd(), path)
						paths.append(joined)
	except FileNotFoundError:
		print(directory, "does not exist.")
	except NotADirectoryError:
		print(directory, "is not a directory.")

	return paths

paths2 = all_paths_2(dummypath, ".py")
#print("*\n*\n*\nOutput from recursive directory search:")
#for path in paths2:
	#print(path)

print("Are the outputs from the two search methods identical?", sorted(paths1) == sorted(paths2))

def find_duplicates(dirname):
	"""
	Recognizes duplicate files within the directory specified by dirname.
	"""
	duplicates = []

	try:
		paths = []
		w = tuple(os.walk(dirname))
		for i in range(len(w)): # cycles through the given directory plus all subdirectories
			currdir = w[i][0]
			names = w[i][2]
			for name in names:
				joined = os.path.join(currdir, name)
				paths.append(joined)

		cmd_list = ['certutil -hashfile \"%s\" MD5' %path for path in paths] # must addquotation marks around the path 		# because some filenames have spaces in them, and that makes the command prompt think it's multiple arguments
		identities = []

		for cmd in cmd_list:
			fp = os.popen(cmd)
			txt = fp.read().split("\n") # generates some text we don't need
			fpath = txt[0] # before the first \n, there's some text that includes the filepath
			fpath = fpath.removeprefix("MD5 hash of ")
			fpath = fpath.removesuffix(":")
			checksum = txt[1] # checksum is embedded between the first and second \n
			identities.append((fpath, checksum)) 
		stat = fp.close()
		for i in range(len(identities)-1):
			j = i+1
			while j < len(identities):
				if identities[i][1] == identities[j][1]: # now compare the checksums
					duplicates.append((identities[i][0], identities[j][0])) # if checksums identical, 
					# then append the two filepaths to duplicates as a tuple
				j += 1
	except FileNotFoundError:
		print(directory, "does not exist.")
	except NotADirectoryError:
		print(directory, "is not a directory.")

	return duplicates

print(find_duplicates(dummypath))