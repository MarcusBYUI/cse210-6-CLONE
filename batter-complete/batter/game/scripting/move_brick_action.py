from constants import *
from game.casting.point import Point
from game.scripting.action import Action

class MoveBrickAction(Action):
    def execute(self, cast, script):
        """Executes the move brick action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """ 

        brick = cast.get_first_actor(BRICK_GROUP)
        body = brick.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - BRICK_WIDTH):
            position = Point(SCREEN_WIDTH - CHICKEN_WIDTH, position.get_y())
            
        body.set_position(position)       
        self._move_brick(cast)

    def _move_brick(self, cast):
        """Move the car along the road
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        bricks = cast.get_actors("brick")
        for brick in BRICK_GROUP:
            brick.move_next()