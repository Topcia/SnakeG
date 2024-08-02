from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

#        Screen Options:
#################################
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
#################################
#################################
game_is_on = True

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 20:
        food.reload()
        snake.grow()
        score.change()

    for segment in snake.snake_parts[1:]:

        if snake.head.distance(segment) < 15:
            snake.reset()
            score.reset_score()
            time.sleep(1)



    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        snake.reset()
        score.reset_score()
        time.sleep(1)
screen.exitonclick()
