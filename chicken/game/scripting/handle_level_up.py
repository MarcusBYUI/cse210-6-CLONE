from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService
from game.scripting.handle_restart_action import HandleRestartAction
from game.casting.car import Car
from game.casting.log import Log

import time

class HandleLevelUp(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the chicken collides with cars or other harmful items, and the chicken loses a life.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._level_up = False
        self._keyboard_service = KeyboardService()
        self._action = HandleRestartAction(self._keyboard_service)
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._level_up:

            self._check_level_up(cast)
            
            if self._level_up:
                self._prepare_levelup(cast, script)
                
        else:
            time.sleep(3)
            message = cast.get_last_actor("messages")
                
            message.set_text("")
            self._do_level_up(cast, script)


    
    def _check_level_up(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        chicken = cast.get_first_actor("chicken")
        if chicken.get_position().get_y() == 50:
            self._level_up = True
        
                
    def _do_level_up(self, cast, script):
        
        level = cast.get_first_actor("level")
        level.next_level()
        
        next_level = level.get_level()
        level.set_text(f"Level: {next_level}")
        
        chicken = cast.get_first_actor("chicken")
        chicken.set_position(Point(int(MAX_X/2), int(MAX_Y - 30)))
        
    
        cast.remove_group("car")
        cast.remove_group("log")
        #car lane 1
        cast.add_actor("car", Car(2, CAR_LANE_ONE, next_level))
        #car lane 2
        cast.add_actor("car", Car(1, CAR_LANE_TWO, next_level))
        #car lane 3
        cast.add_actor("car", Car(3, CAR_LANE_THREE, next_level))
        #car lane 4
        cast.add_actor("car", Car(4, CAR_LANE_FOUR, next_level))
        #car lane 5
        cast.add_actor("car", Car(5, CAR_LANE_FIVE, next_level))
        
        #Water Log
        cast.add_actor("log", Log(2, LOG_LANE_THREE, next_level))
        cast.add_actor("log", Log(1, LOG_LANE_TWO, next_level))
        cast.add_actor("log", Log(3, LOG_LANE_ONE, next_level))
        cast.add_actor("log", Log(4, LOG_LANE_FOUR, next_level))
        cast.add_actor("log", Log(5, LOG_LANE_FIVE, next_level))        
        self._level_up = False
        
        
        
        
    def _prepare_levelup(self, cast, script):
        if self._level_up:
            
            message = Actor()
            x = int(MAX_X / 2)
            y = int(10)
            position = Point(x, y)
            message.set_position(position)
            
            
            message.set_text("Level Completed!!, Brace for the Next Level")  
            message.set_font_size = 20
            
            
                
            cast.add_actor("messages", message)                
    
            self._level_up = True
        