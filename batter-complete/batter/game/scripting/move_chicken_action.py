from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveChickenAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        chicken = cast.get_first_actor(CHICKEN_GROUP)
        body = chicken.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - CHICKEN_WIDTH):
            position = Point(SCREEN_WIDTH - CHICKEN_WIDTH, position.get_y())
            
        body.set_position(position)
        