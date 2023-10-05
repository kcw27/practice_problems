def wrap(s, n):
	"""
	In printing a long string s, wraps it so that each line has at most n characters.
	"""

	if len(s) > n:
		print(s[:n]) # print the first n characters of those remaining
		wrap(s[n:], n) # process the rest of the string
	else: # the string is now short enough to right-justify
		right_justify(s)


def right_justify(s):
	"""
	Prints string s with leading spaces, such that the last letter of s is in column 70.
	"""

	if len(s) > 70: # if the string is too long, need to wrap it
		wrap(s, n=70)
	else:
		spaces = 70 - len(s)
		justified = ' ' * spaces + s
		print(justified)


right_justify('python')

right_justify('Using the command prompt is fun')

print()
long_string = "Let me see. Alas, poor Yorick! I knew him, Horatio, a fellow of infinite jest, of most excellent fancy. He hath borne me on his back a thousand times, and now, how abhorred in my imagination it is! My gorge rises at it. Here hung those lips that I have kissed I know not how oft. Where be your gibes now? Your gambols? Your songs? Your flashes of merriment that were wont to set the table on a roar? Not one now to mock your own grinning? Quite chapfallen? Now get you to my lady's chamber and tell her, let her paint an inch thick, to this favor she must come. Make her laugh at that. Prithee, Horatio, tell me one thing."
right_justify(long_string)
