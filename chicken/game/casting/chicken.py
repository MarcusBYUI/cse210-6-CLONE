from constants import *
from game.casting.actor import Actor
from game.shared.point import Point


class Chicken(Actor):
    """
    A Cycle is a wheeled vehicle that leaves a trail behind it to indicate the path it has taken.
    
    The responsibility of Chicken is to move itself.

    Attributes:
        _points (int): The number of points the collision is worth.
    """
    def __init__(self):
        super().__init__()
        self._prepare_body()



    
    def _prepare_body(self):

        self._text = "#"
        self._font_size = 30
        x = int(MAX_X / 2)
        y = int(MAX_Y - 30)
        position = Point(x, y)
        self._position = position
        self._id = "robot"