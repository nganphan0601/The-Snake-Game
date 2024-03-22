from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 
 
WIDTH = 700
HEIGHT = 700
BORDER_TR = WIDTH/2 - 5
BORDER_DL = (WIDTH/2 - 5) * -1

# Screen setup
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Start game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()
        
    # Detect collision with wall
    if snake.head.xcor() > BORDER_TR or snake.head.xcor() < BORDER_DL or snake.head.ycor() > BORDER_TR or snake.head.ycor() < BORDER_DL:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            game_is_on = False
            scoreboard.game_over()


screen.mainloop()