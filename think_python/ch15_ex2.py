import ch15_ex1 as geo
import ch4_mypolygon as mypolygon
import turtle
import copy

def draw_rect(t, r, reset_position=True):
	"""
	Uses Turtle t to draw Rectangle r.
	If reset_position==True, then navigates t back to its starting point. Useful if relying on coordinate system.
	"""
	# first navigate to the lower left corner
	t.pu()
	t.fd(r.corner.x) # turtle seems to face right initially, so it moves in the x direction
	t.lt(90) # now time to navigate in the y direction
	t.fd(r.corner.y)

	# now draw the rectangle
	# turtle's currently facing up (even if r.corner.y was negative)
	t.pd()
	for d in [r.height, r.width, r.height, r.width]:
		t.fd(d)
		t.rt(90)

	if reset_position:
		t.pu()
		t.lt(90)
		t.fd(r.corner.x)
		t.lt(90)
		t.fd(r.corner.y)
		t.lt(90) # reset the direction that t is facing

def draw_circle(t, c, reset_position=True):
	"""
	Uses Turtle t to draw Circle c.
	If reset_position==True, then navigates t back to its starting point. Useful if relying on coordinate system.
	"""
	# first navigate to the rightmost point on the circle
	t.pu()
	t.fd(c.center.x + c.radius)
	t.lt(90)
	t.fd(c.center.y)

	# now draw the circle
	mypolygon.circle(bob, c.radius)

	if reset_position:
		t.pu()
		t.lt(90)
		t.fd(c.center.x + c.radius)
		t.lt(90)
		t.fd(c.center.y)
		t.lt(90) # reset the direction that t is facing

if __name__ == "__main__":
	circ = geo.Circle()
	circ.center.x, circ.center.y, circ.radius = 150, 100, 75

	box4 = geo.Rectangle()
	box4.corner = geo.Point()
	box4.width, box4.height, box4.corner.x, box4.corner.y = 50.0, 50.0, 125, 175

	box5 = geo.move_rectangle2(box4, 0, 100)
	box6 = geo.move_rectangle2(box4, 0, -3)

	bob = turtle.Turtle()
	draw_rect(bob, box4)
	draw_rect(bob, box6)
	draw_rect(bob, box5)
	draw_circle(bob, circ)
	turtle.mainloop()