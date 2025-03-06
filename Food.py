from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.go_to_random_location()


    def go_to_random_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.teleport(x=random_x, y=random_y)
