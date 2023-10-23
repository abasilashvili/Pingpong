from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(270)
        self.goto(x_pos, y_pos)

    def go_up(self):
        self.backward(20)

    def go_down(self):
        self.forward(20)

