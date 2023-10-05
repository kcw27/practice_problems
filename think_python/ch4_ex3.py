import turtle
import math
import ch4_mypolygon


def isosceles(t, r, length, angle):
	"""
	Draws an isosceles triangle.
	t: Turtle object
	r:  two sides have this length
	length: one side has this length
	angle: between the two sides of length r (computed in turtlepies())
	"""
	other_angle = (180-angle)/2

	ch4_mypolygon.polyline(t, r, angle=180-other_angle, n=1) 
	ch4_mypolygon.polyline(t, length, angle=180-other_angle, n=1)
	ch4_mypolygon.polyline(t, r, angle=180-other_angle, n=1)

def turtlepies(t, length, n):
	"""
	Draws a regular polygon, segmented into isosceles triangles.
	t = Turtle object
	length = length of each exterior side of the polygon
	n = number of sides of the polygon
	"""
	angle = 360 / n
	r = length / (2 * math.sin((angle/2) * (math.pi/180))) # length of two sides in isosceles triangle; last term converts angle to radians

	for i in range(n):
		isosceles(t, r, length, angle) # draws the triangle inside the pie
		t.lt((180-angle)/2)
	

bob = turtle.Turtle()

turtlepies(bob, 150, 5)
turtlepies(bob, 200, 10)

turtle.mainloop()