from turtle import Turtle

class Scoreboard(Turtle):
	"""Create Scoreboard Object to display on screen"""
	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		text = f"Score: {self.score}"
		self.penup()
		self.goto(0,260)
		self.write(arg=text, align="center", font=("Arial", 24, "normal"))
		self.hideturtle()


	def increase_score(self):
		"""increase the score by 1 after each food eating"""
		self.clear()
		self.score += 1
		text = f"Score: {self.score}"
		self.write(arg=text, align="center", font=("Arial", 24, "normal"))

	def game_over(self):
		"""Print Game Over message"""
		self.goto(0,0)
		self.write("Game Over", align="center", font=("Arial", 24, "normal"))

