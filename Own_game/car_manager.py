from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_turtles = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_turtle(self):
        chance = random.randint(1, 7)
        if chance == 1:
            new_turtle = Turtle("turtle")
            new_turtle.penup()
            new_turtle.color(random.choice(COLORS))
            new_turtle.setheading(90)
            new_turtle.shapesize(stretch_wid=2, stretch_len=1)
            random_x = random.randint(-245, 250)
            new_turtle.goto(random_x, -300)
            self.all_turtles.append(new_turtle)

    def movement(self):
        for turtle in self.all_turtles:
            turtle.forward(self.speed)

    def increase_movement(self):
        self.speed += MOVE_INCREMENT
