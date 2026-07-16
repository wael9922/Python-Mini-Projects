from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
# setting up th screen size
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

# creating the game objects
snake = Snake()
food = Food()
score = Scoreboard()

# setting up the game keys
screen.listen()
screen.onkey(key="w",fun=snake.up) # up
screen.onkey(key="s",fun=snake.down) # down
screen.onkey(key="d",fun=snake.right) # right
screen.onkey(key="a",fun=snake.left) # left


game_on = True

while game_on:
	screen.update()
	time.sleep(0.1)
	snake.move()
	# detect when the snake eat a food
	if snake.head.distance(food) < 15:
		food.refresh() # food respawn in random positions
		score.increase_score() # add score
		snake.extend() # extend the snake length

	# check if the snake hit a wall
	if(
		snake.head.xcor() > 290 or
		snake.head.xcor() < -290 or
		snake.head.ycor() > 290 or
		snake.head.ycor() < -290
	):
		game_on = False # end the game
		score.game_over()

	for segment in snake.segments[1:]:
		# detect if the snake head hit the tail
		if snake.head.distance(segment) <10:
			game_on = False  # end the game
			score.game_over()


screen.exitonclick()