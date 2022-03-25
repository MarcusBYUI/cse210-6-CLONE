from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Chicken(Actor):
    """A character that hops across the road in the game. 
    
    The responsibility of Chicken is to move itself.

    Attributes:
        _points (int): The number of points the hop forward is worth.
    """
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Chicken.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the chicken's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the chicken's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the chicken using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def hop_up(self):
        """Moves the chicken up."""
        velocity = Point(0, -CHICKEN_VELOCITY)
        self._body.set_velocity(velocity)

    def hop_down(self):
        """Moves the chicken down."""
        velocity = Point(0, CHICKEN_VELOCITY)
        self._body.set_velocity(velocity)

    def hop_left(self):
        """Steers the chicken to the left."""
        velocity = Point(-CHICKEN_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def hop_right(self):
        """Steers the chicken to the right."""
        velocity = Point(CHICKEN_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the chicken from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)