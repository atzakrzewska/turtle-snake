import random
from turtle import Turtle

FOOD_COUNT = 1


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("tomato3")
        self.speed(10)
        self.refresh()

    def refresh(self):
        random_x = random.choice(range(-280, 280, 20))
        random_y = random.choice(range(-260, 260, 20))
        self.goto(random_x, random_y)
