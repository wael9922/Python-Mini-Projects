from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)   # window size
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Game objects
right_paddle = Paddle(position=350, speed=30)
left_paddle = Paddle(position=-350, speed=30)
ball = Ball()
scoreboard = Scoreboard()

# Create a button to start the game
start_message = Turtle()
start_message.color("white")
start_message.penup()
start_message.hideturtle()
start_message.goto(0, 0)
start_message.write("Press SPACE to Start", align="center", font=("Arial", 24, "normal"))

screen.listen()

game_on = False

def start_game():
    global game_on
    game_on = True
    start_message.clear()

def pause_game():
    """pause the game"""
    global game_on
    game_on = False
    start_message.goto(0, 0)
    start_message.write("Game Paused - Press SPACE to Resume", align="center", font=("Arial", 20, "normal"))

screen.onkey(fun=pause_game, key="Escape")
screen.onkey(fun=start_game, key="space")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")

while True:
    if game_on:
        time.sleep(0.1)  # control the ball speed
        screen.update()
        ball.move()

        # wall collision
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # paddles collision
        # Right paddle collision (ball moving right)
        if ball.xcor() > 320 and ball.distance(right_paddle) < 50 and ball.x > 0:
            ball.bounce_x()

        # Left paddle collision (ball moving left)
        if ball.xcor() < -320 and ball.distance(left_paddle) < 50 and ball.x < 0:
            ball.bounce_x()

        if ball.xcor() > 370:
            ball.reset_position()
            scoreboard.left_point()

        if ball.xcor() < -370:
            ball.reset_position()
            scoreboard.right_point()
    else:
        screen.update()

screen.exitonclick()