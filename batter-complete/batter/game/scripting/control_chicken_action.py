from constants import *
from game.scripting.action import Action


class ControlChickenAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        chicken = cast.get_first_actor(CHICKEN_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            chicken.hop_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            chicken.hop_right() 
        elif self._keyboard_service.is_key_down(UP): 
            chicken.hop_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            chicken.hop_down()
        else: 
            chicken.stop_moving()        