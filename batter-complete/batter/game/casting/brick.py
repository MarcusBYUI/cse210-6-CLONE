from game.casting.actor import Actor
from game.casting.point import Point
from constants import *
from random import *


class Brick(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, debug = False):
        """Constructs a new Brick.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        # self._animation = animation
        # self._points = points
        
    def get_animation(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
            """
        

         
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)
        
        for brick in self._bricks:
            x = (self._body.get_position().get_x() - (self._speed * self.level)) % MAX_X
            y = self._body.get_position().get_y()

            
            self._body.set_position(Point(x, y))
        
    # def get_cars(self):
    #     return self._cars
    
    def stop_cars(self):
        self._speed = 0