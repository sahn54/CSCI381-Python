from turtle import Turtle


STARTING_POSITION = (-280, 0)
MOVE_DISTANCE = 10
FINISH_LINE_X = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.starting_position()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def finish_line_reached(self):
        if self.xcor() > FINISH_LINE_X:
            return True
        else:
            return False
