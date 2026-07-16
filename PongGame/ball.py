from turtle import Turtle

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color("white")
		self.penup()
		self.x = 15 # control the ball speed
		self.y = 15 # control the ball speed

	def move(self):
		"""move the ball"""
		new_x = self.xcor() + self.x
		new_y = self.ycor() + self.y
		self.goto(new_x, new_y)

	def bounce_y(self):
		"""bounce the ball against top and bottom walls"""
		self.y *= -1

	def bounce_x(self):
		"""bounce the ball after the paddles hit it"""
		self.x *= -1

	def reset_position(self):
		"""reset the ball to the center after each point scored"""
		self.goto(0, 0)
		self.bounce_x()