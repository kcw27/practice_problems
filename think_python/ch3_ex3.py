# First, the most general versions of the functions, which allow the user to control not only the dimensions of the grid, but also of individual cells in the grid.
def draw_row_scalable(cols, cell_size):
	"""
	Draws a row of symbols for the grid.
	cols: the number of columns to be drawn. Length of each line is determined by number of columns.
	cell_size: the width of each cell.
	"""
	for i in range(cols): # the range function is non-inclusive, so no need to subtract 1
		print('+', '-' * cell_size, end = ' ')
	print('+') # fence-posting

def draw_col_scalable(cols, cell_size):
	"""
	Draws segments of columns, done row by row. For use in draw_grid() and draw_square_grid().
	cols: the number of columns to be drawn. Length of each line is determined by number of columns.
	cell_size: the height of each cell.
	"""
	for i in range(cols):
		print('/', ' ' * cell_size, end = ' ')
	print('/') # fence-posting

def draw_grid_scalable(rows, cols, cell_width, cell_height):
	"""
	Draws a grid with the given number of rows and columns.
	Cells in the grid have dimensions of cell_width and cell_height.
	"""
	for i in range(rows):
		draw_row_scalable(cols, cell_width)
		for j in range(cell_height):
			draw_col_scalable(cols, cell_width)
	draw_row_scalable(cols, cell_width)

print("Cell dimensions can be set when drawing grids with draw_grid_scalable().")
draw_grid_scalable(2, 2, 4, 4)
draw_grid_scalable(2, 2, 5, 2)
draw_grid_scalable(2, 3, 3, 6)
draw_grid_scalable(3, 2, 4, 2)
draw_grid_scalable(4, 4, 1, 7)


# A clean interface allows the user to do what they want without dealing with unnecessary details. 
# The set of functions below are less general, but less hassle to use because the cell_size parameter is set by default. 

def draw_row(cols):
	"""
	Draws a row of symbols for the grid. For use in draw_grid() and draw_square_grid().
	cols: the number of columns to be drawn. Length of each line is determined by number of columns.
	"""
	draw_row_scalable(cols, 4)

def draw_col(cols):
	"""
	Draws segments of columns. For use in draw_grid() and draw_square_grid().
	cols: the number of columns to be drawn. Length of each line is determined by number of columns.
	"""
	draw_col_scalable(cols, 4)

def draw_grid(rows, cols, square=None):
	"""
	Draws a grid with the given number of rows and columns.
	If optional parameter square==True, then cells will be drawn to look square.
	"""
	col_height=4 # default value
	if square==True:
		col_height=2 # if there are 2, not 4, "column" lines per row line, then individual cells look square

	for i in range(rows):
		draw_row(cols)
		for j in range(col_height):
			draw_col(cols)
	draw_row(cols)

print("draw_grid() frees the user from having to manually set cell dimensions.")
draw_grid(2, 2)
draw_grid(2, 3)
draw_grid(3, 2)
draw_grid(4, 4)

print("Let's redraw these grids with more square-looking cells.")
draw_grid(2, 2, square=True)
draw_grid(2, 3, square=True)
draw_grid(3, 2, square=True)
draw_grid(4, 4, square=True)

