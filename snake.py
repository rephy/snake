from turtle import Turtle, Screen
from time import sleep

class Snake:

    def __init__(self):
        self.game = True

        self.start_positions = [(20, 0), (0, 0), (-20, 0)]

        self.segments = []

        self.incoming_segments = []

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake - by Raphael M.")
        self.screen.tracer(0)

        self.setup_snake()

        self.screen.listen()

        self.screen.onkey(key="d", fun=self.turn_right)
        self.screen.onkey(key="Right", fun=self.turn_right)
        self.screen.onkey(key="a", fun=self.turn_left)
        self.screen.onkey(key="Left", fun=self.turn_left)
        self.screen.onkey(key="w", fun=self.turn_up)
        self.screen.onkey(key="Up", fun=self.turn_up)
        self.screen.onkey(key="s", fun=self.turn_down)
        self.screen.onkey(key="Down", fun=self.turn_down)

    def setup_snake(self):
        for n in range(3):
            t = Turtle()
            t.shape("square")
            t.color("white")
            t.penup()
            t.goto(self.start_positions[n][0], self.start_positions[n][1])
            self.segments.append(t)

    def move(self):
        for n in range(len(self.segments)):
            segment = self.segments[n]
            if n + 1 != len(self.segments):
                target = self.segments[n + 1]
                segment.goto(target.xcor(), target.ycor())
                self.screen.update()
            else:
                segment.forward(20)

            self.new_part()

    def turn_left(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 0:
            head.speed(10000)
            head.setheading(180)
            head.speed(3)

    def turn_right(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 180:
            head.speed(10000)
            head.setheading(0)
            head.speed(3)

    def turn_up(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 270:
            head.speed(10000)
            head.setheading(90)
            head.speed(3)

    def turn_down(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 90:
            head.speed(10000)
            head.setheading(270)
            head.speed(3)

    def new_part_incoming(self):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.speed(10000)
        t.goto(self.segments[0].xcor(), self.segments[0].ycor())
        t.speed(3)
        self.incoming_segments.append(t)

    def new_part(self):
        for t in self.incoming_segments:
            self.segments.insert(0, t)
            self.incoming_segments = []

    def exit(self):
        self.screen.exitonclick()