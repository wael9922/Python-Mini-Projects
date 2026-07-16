from turtle import Turtle

class Paddle(Turtle):
	"""Create the paddle"""
	def __init__(self, position, speed):
		super().__init__()
		self.speed = speed
		self.shape("square")
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.penup()
		self.goto(position, 0)

	def up(self):
		"""Move the paddle up"""
		new_y = self.ycor() + self.speed
		self.goto(self.xcor(), new_y)

	def down(self):
		"""Move the paddle down"""
		new_y = self.ycor() - self.speed
		self.goto(self.xcor(), new_y)
