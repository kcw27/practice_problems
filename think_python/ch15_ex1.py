import math
import copy

class Point:
	"""Represents a point in 2-D space."""
	x = 0.0
	y = 0.0

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(p1, p2):
	"""
	Takes two Points as an argument and returns the distance between them.
	"""
	dx = p1.x-p2.x
	dy = p1.y-p2.y

	return math.sqrt(dx**2 + dy**2)


class Rectangle:
	"""Represents a rectangle. 

	attributes: width, height, corner.
	corner is a Point that specifies the lower left corner.
	"""

def move_rectangle(rect, dx, dy):
	"""
	Moves rectangle rect by distances dx and dy in the x and y directions, respectively.
	"""
	rect.corner.x += dx
	rect.corner.y += dy

def move_rectangle2(rect, dx, dy):
	"""
	Version of move_rectangle that creates and returns a new rectangle instead of modifying rect.
	"""
	rect2 = copy.deepcopy(rect)

	rect2.corner.x += dx
	rect2.corner.y += dy

	return rect2

class Circle:
	"""
	Attributes: center (Point object) and radius (a number)
	"""
	center = Point()
	radius = 0

def point_in_circle(c, p):
	"""
	Returns True if Point p lies in or on the boundary of Circle c.
	"""
	d = distance_between_points(p, c.center)
	return d <= c.radius # if the distance from p to the center isn't bigger than the radius, p's in c

def get_corners(r):
	"""
	Returns a tuple containing the four corners of a Rectangle in this order:
	bottom left, bottom right, top left, top right
	"""
	# find the other corners of the rectangle (r.corner is the bottom left corner)
	corner2, corner3, corner4 = copy.copy(r.corner), copy.copy(r.corner), copy.copy(r.corner)

	# copying so we don't change r.corner itself (no need to deep-copy; Points don't reference other objects)
	corner2.x += r.width # bottom right
	corner3.y += r.height # top left
	corner4.x += r.width
	corner4.y += r.height # top right)

	return r.corner, corner2, corner3, corner4

def rect_in_circle(c, r):
	"""
	Returns True if Rectangle r lies entirely in or on the boundary of Circle c.
	"""
	corners = get_corners(r)
	for corn in corners:
		if not point_in_circle(c, corn):
			return False
	return True

def rect_circle_overlap(c, r):
	"""
	Returns True if any corner of Rectangle r falls inside Circle C.
	"""
	corners = get_corners(r)
	for corn in corners:
		if point_in_circle(c, corn):
			return True
	return False

def traverse_line(p1, p2, c, p0 = None):
	"""
	Helper function for rect_circle_overlap2. 
	Traverses the line between p1 and p2, checking if any points are in Circle c.
	p0 is a Point denoting progress along the path from p1 to p2
	"""
	if p0 == None:
		p0 = copy.copy(p1)

	if point_in_circle(c, p0):
		return True
	elif abs(p0.x-p2.x) < 0.01 and abs(p0.y-p2.y) < 0.01: # give up if the whole line's been traversed
		return False
	else:
		p0.x += -0.1 * (p1.x - p2.x) # dx is positive if p1 < p2, negative if p1 > p2
		p0.x += -0.1 * (p1.y - p2.y) # same goes for dy
		return(traverse_line(p1, p2, c, p0))

def rect_circle_overlap2(c, r):
	"""
	Returns True if any part of Rectangle r falls inside Circle C.
	The approach works, it's just inefficient. (Often exceeds max recursion depth)
	"""
	# first check the corners
	corner2, corner3, corner4 = copy.deepcopy(r.corner), copy.deepcopy(r.corner), copy.deepcopy(r.corner)
	# deep-copying so we don't change r.corner itself
	corner2.x += r.width # bottom right
	corner3.y += r.height # top left
	corner4.x += r.width
	corner4.y += r.height

	for corn in [r.corner, corner2, corner3, corner4]:
		#print_point(corn)
		if point_in_circle(c, corn):
			return True

	# now check for overlap along each side of r
	# sides lie between these pairs: 
	# r.corner & corner2
	if traverse_line(r.corner, corner2, c):
		return True
	# r. corner & corner3
	elif traverse_line(r.corner, corner3, c):
		return True
	# corner2 & corner4
	elif traverse_line(corner2, corner4, c):
		return True
	# corner3 & corner4
	elif traverse_line(corner3, corner4, c):
		return True
	else:
		return False



if __name__ == '__main__':
	# working with Points
	blank = Point()
	blank.x, blank.y = 3.0, 4.0
	blank2 = Point()
	#print(distance_between_points(blank, blank2))

	# working with Rectangles
	box = Rectangle()
	box.width, box.height, box.corner = 100.0, 200.0, Point()

	box2 = copy.deepcopy(box)
	box2.width, box2.height = 50.0, 50.0

	print("Corner of box before moving:", end=" ")
	print_point(box.corner)
	move_rectangle(box, 10, 20)
	print("Corner of box after moving 10 units in the x direction and 20 units in the y direction:", end=" ")
	print_point(box.corner)

	# working with Circles
	circ = Circle()
	circ.center.x, circ.center.y, circ.radius = 150, 100, 75
	print("\nCircle has a radius of ", circ.radius, " and is centered on (", circ.center.x, ", ", circ.center.y, ").", sep="")


	p_1, p_2, p_3 = Point(), Point(), Point()
	p_2.x, p_2.y = 150, 25
	p_3.x, p_3.y = 150, 24

	for p in [p_1, p_2, p_3]:
		print("Point:", end=" ")
		print_point(p)
		print("Is this point in the circle?", point_in_circle(circ, p), end="\n\n")

	# Rectangle and Circle overlap

	box3 = move_rectangle2(box2, 125, 75)

	for b in [box, box2, box3]:
		print("Rectangle's corners:")
		for corn in get_corners(b):
			print_point(corn)
		print("Is this rectangle fully inside the circle?", rect_in_circle(circ, b), end="\n\n")

	print("Box 3 has corner(s) in circle:", rect_circle_overlap(circ, box3))
	box4 = move_rectangle2(box3, 0, 100)
	print("Box 4's bottom left corner:", end=" ")
	print_point(box4.corner)
	print("Box 4's width: ", box4.width)
	print("Box 4's height: ", box4.height)
	print("Box 4 has corner(s) in circle:", rect_circle_overlap(circ, box4))
	box5 = move_rectangle2(box4, 0, 100)
	print("Box 5 has corner(s) in circle:", rect_circle_overlap(circ, box5))
	
	print("Box 3 overlaps with circle:", rect_circle_overlap(circ, box3))
	print("Box 4 overlaps with circle:", rect_circle_overlap2(circ, box4))
	box6 = move_rectangle2(box4, 0, -3)
	print("Box 6 overlaps with circle:", rect_circle_overlap2(circ, box6))

	# can't run this with box5 because then Python complains about recursion depth
	# but notice that it works with box 4 (and also with box 6, which is box 4 slightly shifted down)
	# I think the issue is that box5 doesn't overlap with the circle at all, so the code just runs too many times