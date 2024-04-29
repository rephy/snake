from turtle import Turtle

class Texts(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.goto(0, 250)
        self.speed("fastest")
        self.color("white")

    def keep_score(self, score):
        self.clear()
        self.write(f"Score: {score}", font=("Verdana", 20, "bold"), align="center")

    def game_over(self):
        self.speed(10000)
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.speed(3)
        self.write("Game over!", font=("Verdana", 35, "bold"), align="center")