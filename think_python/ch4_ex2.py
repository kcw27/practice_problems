import turtle
import math
import ch4_mypolygon

def petal(t, r, angle):
	"""
	Draws a single petal using arcs (from the ch4_mypolygon module).
	t is a Turtle.
	r is the radius of circle calculated from the length and width arguments in flowers().
	angle is the angle to traverse in the circle of radius r, also calculated from length and width.
	"""
	for i in range(2):
		ch4_mypolygon.arc(t, r, angle)
		t.lt(180-angle)

def flowers(t, length, width, num):
	"""
	Draws a flower of num petals. Each petal has the given length and width. 
	For shapes to be drawn accurately, width must be less than length. 
	This is because petals are drawn using arcs from a circle, and for circles it is impossible for an arc to be so convex that its width exceeds its chord length. 
	t is a Turtle.
	"""
	# after some geometry and algebra, I calculated the radius for the circle that is partially traversed when drawing arcs to achieve the given length and width of petals.
	r = (width**2 + length**2) / (4*width)
	# I also calculated the angle to use for drawing arcs to make petals.
	angle = 2 * math.asin((length/2) / r) * (180/math.pi) # that last term is to convert from radians to degrees.

	step_angle = 360 / num # angle to rotate by after drawing each petal. In the end, a full 360 degrees is traversed.

	for i in range(num):
		petal(t, r, angle)
		t.lt(step_angle)

bob = turtle.Turtle()

flowers(bob, length=10, width=5, num=6)
flowers(bob, length=30, width=2, num=14) # not advised to go much bigger than this length of petal

turtle.mainloop()