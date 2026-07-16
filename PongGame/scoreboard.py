from turtle import Turtle

class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.color("white")
		self.penup()
		self.hideturtle()
		self.left_score = 0
		self.right_score = 0
		self.update_scoreboard()

	def left_point(self):
		"""Add point to the left player"""

		self.left_score += 1
		self.update_scoreboard()

	def right_point(self):
		"""Add point to the right player"""
		self.right_score += 1
		self.update_scoreboard()

	def update_scoreboard(self):
		"""Update the scoreboard with any score changes"""
		self.clear()
		self.goto(-100,200)
		self.write(self.left_score, align="center", font=("courier", 80, "normal"))
		self.goto(100,200)
		self.write(self.right_score, align="center", font=("courier", 80, "normal"))






