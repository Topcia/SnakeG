from turtle import Turtle

# Constants:
MOVE_DISTANCE = 20
START_POS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_parts = []
        self.place()
        self.head = self.snake_parts[0]

    def place(self):
        for pos in START_POS:
            snake_part = Turtle(shape="square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(pos)
            self.snake_parts.append(snake_part)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for snake_part in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[snake_part].goto(x=self.snake_parts[snake_part - 1].xcor(),
                                              y=self.snake_parts[snake_part - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def grow(self):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        location = self.snake_parts[len(self.snake_parts) - 1].pos()
        snake_part.goto(location)
        self.snake_parts.append(snake_part)

    def reset(self):
        for snake_part in self.snake_parts:
            snake_part.reset()
        self.snake_parts.clear()
        self.place()
        self.head = self.snake_parts[0]
