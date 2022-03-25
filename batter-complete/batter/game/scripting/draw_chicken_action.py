from constants import *
from game.scripting.action import Action


class DrawChickenAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        chicken = cast.get_first_actor(CHICKEN_GROUP)
        body = chicken.get_body()

        if chicken.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = chicken.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)