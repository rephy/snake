from turtle import Turtle, Screen
from time import sleep

class Snake:

    def __init__(self):
        self.game = True

        self.start_positions = [(-20, 0), (0, 0), (20, 0)]

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
            t.speed(10000)
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

        self.check_self_collision()
        self.check_wall_collision()

        self.new_part()

    def turn_left(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 0 and round(head.heading()/90) == head.heading()/90:
            head.setheading(180)

    def turn_right(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 180 and round(head.heading()/90) == head.heading()/90:
            head.setheading(0)

    def turn_up(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 270 and round(head.heading()/90) == head.heading()/90:
            head.setheading(90)

    def turn_down(self):
        head = self.segments[len(self.segments) - 1]
        if head.heading() != 90 and round(head.heading()/90) == head.heading()/90:
            head.setheading(270)

    def new_part_incoming(self):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.speed(10000)
        t.goto(self.segments[0].xcor(), self.segments[0].ycor())
        self.incoming_segments.append(t)

    def new_part(self):
        for t in self.incoming_segments:
            self.segments.insert(0, t)
            self.incoming_segments = []

    def check_self_collision(self):
        segment_positions = []
        none_duplicate_segment_positions = []

        for segment in self.segments:
            segment_positions.append(segment.pos())

            duplicate_exists = False

            for not_duplicate_segment in none_duplicate_segment_positions:
                if segment.pos() == not_duplicate_segment:
                    duplicate_exists = True

            if duplicate_exists == False:
                none_duplicate_segment_positions.append(segment.pos())

        if segment_positions == none_duplicate_segment_positions:
            pass
        else:
            self.game = False

    def check_wall_collision(self):
        if abs(self.segments[len(self.segments) - 1].xcor()) >= 300 or abs(self.segments[len(self.segments) - 1].ycor()) >= 300:
            self.game = False

    def exit(self):
        self.screen.exitonclick()