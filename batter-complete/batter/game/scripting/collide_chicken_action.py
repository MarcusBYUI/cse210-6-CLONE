from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideChickenAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        chicken = cast.get_first_actor(CHICKEN_GROUP)
        chicken = cast.get_first_actor(CHICKEN_GROUP)
        
        chicken_body = chicken.get_body()
        chicken_body = chicken.get_body()

        if self._physics_service.has_collided(chicken_body, chicken_body):
            chicken.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)    