from turtle import Screen, Turtle
import time

screen = Screen()

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

NORTH = 90
EAST = 0
SOUTH = 270
WEST = 180


class Snake:
    def __init__(self):
        self.positions = STARTING_POSITIONS
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("LightPink")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("LightPink")
        segment.penup()
        segment.speed(10)
        segment.goto(position)
        self.segments.append(segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move_north(self):
        if self.head.heading() != SOUTH:
            self.head.seth(NORTH)

    def move_east(self):
        if self.head.heading() != WEST:
            self.head.seth(EAST)

    def move_south(self):
        if self.head.heading() != NORTH:
            self.head.seth(SOUTH)

    def move_west(self):
        if self.head.heading() != EAST:
            self.head.seth(WEST)


class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(10)
        self.color("snow")
        self.hideturtle()
        self.penup()
        self.goto(291, 271)
        self.pendown()
        self.goto(291, -271)
        self.goto(-291, -271)
        self.goto(-291, 271)
        self.goto(291, 271)
