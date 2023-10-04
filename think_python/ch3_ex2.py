def do_twice(f, value):
	"""
	Executes function f twice with argument value.
	"""
	f(value)
	f(value)

def print_spam():
	print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, 'spam') #prints 'spam' four times, each on its own line

def do_four(f, value):
	do_twice(f, value)
	do_twice(f, value)

do_four(print_twice, 'hi')

# generalized version of do_twice()
def do_x_times(f, value, x):
	for i in range(x):
		f(value)

do_x_times(print_twice, "bruce", 3)