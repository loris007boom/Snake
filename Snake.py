from turtle import Turtle


MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        for i in range(0, 3):
            position = (0 - i * 20, 0)
            self.add_part(position)


    def add_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_body.append(snake_part)


    def extend(self):
        last_part_position = self.snake_body[-1].position()
        self.add_part(last_part_position)


    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_num-1].xcor()
            new_y = self.snake_body[body_num-1].ycor()
            self.snake_body[body_num].goto(x=new_x, y=new_y)
        self.head.forward(20)


    def point_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def point_north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def point_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def point_south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


