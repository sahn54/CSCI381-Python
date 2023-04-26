import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
traffic = CarManager()
level = Scoreboard()


screen.listen()
screen.onkey(player.move_forward, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    traffic.create_turtle()
    traffic.movement()

    if player.finish_line_reached():
        player.starting_position()
        traffic.increase_movement()
        level.increase_level()
    for other_turtle in traffic.all_turtles:
        if other_turtle.distance(player) < 20:
            game_is_on = False
            level.game_over()


screen.exitonclick()
