from snake import *
from food import *
from scoreboard import *
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Messages
ate = ["nom nom!", "yum!", "tasty!"]
score.update_scoreboard()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting Collisions with FOOD

    if snake.head.distance(food) < 15:
        score.increasescore()
        snake.extend()
        food.refresh()
        print("nom nom nom")

    # Detecting Collisions with WALL

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        print("oops")
        score.reset()
        snake.reset()

    # Detecting Collisions with TAIL

    for segmento in snake.segment:

        if segmento == snake.head:
            pass
        elif snake.head.distance(segmento) < 10:
            print("oops")
            score.reset()
            snake.reset()

screen.exitonclick()
