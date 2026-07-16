from turtle import Turtle

# Constants
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	"""Create the snake object"""
	def __init__(self):
		self.segments = []
		self.create_snake()
		self.head = self.segments[0]

	def create_snake(self):
		"""Create the starter snake"""
		for position in STARTING_POSITIONS:
			self.add_segment(position)

	def add_segment(self, position):
		"""Add extra segment to the snake (extending length of the snake)"""
		new_segment = Turtle("square")
		new_segment.penup()
		new_segment.color("white")
		new_segment.goto(position)
		self.segments.append(new_segment)

	def extend(self):
		"""Extending length of the snake after each food eating"""
		self.add_segment(self.segments[-1].pos())

	def up(self):
		"""move up"""
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		"""move down"""
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def right(self):
		"""move right"""
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def left(self):
		"""move left"""
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def move(self):
		"""moving with the snake with directions"""
		for segment in range(len(self.segments) - 1, 0, -1):
			new_x = self.segments[segment - 1].xcor()
			new_y = self.segments[segment - 1].ycor()
			self.segments[segment].goto(new_x, new_y)

		self.segments[0].forward(MOVE_DISTANCE)



