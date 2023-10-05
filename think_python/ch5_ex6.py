import turtle

def koch(t, x):
	"""
	Draws a Koch curve with length x.
	t is a Turtle.
	"""

	if x < 3: # to get a bigger, lower-definition (i.e. faster) Koch curve, use a bigger number as the threshold
		t.fd(x)
	else:
		koch(t, x/3)
		t.lt(60)
		koch(t, x/3)
		t.rt(120)
		koch(t, x/3)
		t.lt(60)
		koch(t, x/3)

def snowflake(t, x):
	"""
	Draws three Koch curves to make a snowflake.
	"""

	koch(t, x)
	t.rt(120) # 360 degrees internal angles divided by 3 reps of koch() = 120 degrees turn each time
	koch(t, x)
	t.rt(120)
	koch(t, x)

def quad_type_1(t, x):
	"""
	Draws a quadratic type 1 curve. See https://en.wikipedia.org/wiki/Koch_snowflake#Variants_of_the_Koch_curve
	Drawn with length x. t is a Turtle.
	"""

	if x < 3:
		t.fd(x)
	else:
		quad_type_1(t, x/1.46)
		t.lt(90)
		quad_type_1(t, x/1.46)
		t.rt(90)
		quad_type_1(t, x/1.46)
		t.rt(90)
		quad_type_1(t, x/1.46)
		t.lt(90)
		quad_type_1(t, x/1.46)



bob = turtle.Turtle()
snowflake(bob, 20)
quad_type_1(bob, 7)

turtle.mainloop()