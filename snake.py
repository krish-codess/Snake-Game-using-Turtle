from turtle import *

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.createSnake()
        self.head = self.segment[0]

    # Creates Snake
    def createSnake(self):
        for positions in STARTING_POSITIONS:
            self.addSegment(positions)

    def extend(self):
        self.addSegment(self.segment[-1].position())

    def addSegment(self, positions):
        new_segment = Turtle(shape="square")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(positions)
        self.segment.append(new_segment)

    # Moves Snake
    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = (self.segment[seg - 1]).xcor()
            new_y = (self.segment[seg - 1]).ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE_FORWARD)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.createSnake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
