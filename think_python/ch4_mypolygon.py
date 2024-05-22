import turtle
import math

## To draw straight lines:
def polyline(t, length, n, angle): # n is number of sides
	"""
	Draws a polyline.
	t: Turtle object
	length: length of each line
	n: number of lines to draw
	angle: left turn angle between each line
	"""
	t.pd()
	for i in range(n): # this is where the difference between polygon and polyline arises
		t.fd(length)
		t.lt(angle)

def polygon(t, length, n):
	"""
	Draws a regular polygon with n sides.
	"""
	polyline(t, length, n, angle=360/n)

# Suppose that the user wishes to draw many squares. square() saves the hassle of defining n=4 in polygon calls.
def square(t, length):
	"""
	Draws a square with the given side length.
	"""
	polygon(t, length, 4)


## To draw curves:
def arc(t, r, angle): 
	""" Draws a fraction of a circle.
	t: Turtle object
	r: radius of circle
	angle: angle in degrees. If angle=360, a full circle is drawn.

	This implementation was taken from Downey's solution. See below for my own implementation.
	"""
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1 # number of lines to draw; suggested by Downey because it scales with the arc length
	
	step_length = arc_length / n
	step_angle = angle / n

	polyline(t, length = arc_length, angle = step_angle, n = n)
	
def arc2(t, r, angle):
	""" 
	My own implementation. 
	It suffered some issues with accuracy that were especially apparent when drawing flowers, 
	so I decided to use Downey's implementation instead. It worked well for the flowers, but
	it seems like it didn't work when I ran the code below to draw basic circles and arcs?
	"""
	circumference = 2 * math.pi * r
	fraction_of_circle = angle / 360
	arc_length = circumference * fraction_of_circle
	resolution = 100 # how many polyline calls to make. Analogous to "n" in Downey's implementation.
	# The higher the resolution, the smoother the curve appears, because each individual line is shorter and more lines are drawn.

	polyline(t, length=circumference/resolution, n=int(resolution * fraction_of_circle), angle=360/resolution)

def circle(t, r): # Hint: figure out the circumference of the circle and make sure that length * n = circumference.
	"""
	Draws a circle with radius r. t is a Turtle.
	"""
	#arc(t, r, angle=360)
	arc2(t, r, angle=360)

if __name__ == "__main__":
	bob = turtle.Turtle()
	print(bob)

	# drawing squares
	square(bob, 100)
	square(bob, 200)

	# drawing polygons
	polygon(bob, 100, 3)
	polygon(bob, 200, 5)

	# circle time!
	circle(bob, 100)
	circle(bob, 50)
	circle(bob, 200)

	# arc time!
	arc2(bob, 100, 180)
	arc2(bob, 50, 270)
	arc2(bob, 200, 360)

	# polyline
	polyline(bob, 100, 3, 90) # only three sides of a square

	turtle.mainloop()
