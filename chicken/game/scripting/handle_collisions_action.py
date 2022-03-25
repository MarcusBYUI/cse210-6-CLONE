from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService
from game.scripting.handle_restart_action import HandleRestartAction
from game.casting.car import Car
from game.casting.log import Log
from game.casting.lives import Lives


import time

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collide with their own segments, or the segments of it's opponent, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = "";
        self._keyboard_service = KeyboardService()
        self._action = HandleRestartAction(self._keyboard_service)
    
        

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:

            self._handle_collision(cast)
            lives = cast.get_first_actor("lives") 
            if self._is_game_over:  
                lives.remove_live()
                lives.set_text(f"Lives: {lives.get_lives()}") 
                
                if lives.get_lives() <= 0:
                    self._handle_game_over(cast, script)  
                else:
                    self._handle_life_loss(cast, script) 
            
            
        else: 
            lives = cast.get_first_actor("lives") 
            
            if lives.get_lives() <= 0:
                self._restart(cast, script)
                
            else:
                self._continue(cast, script)
                
                
                
                


    
    def _handle_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        car_rows = cast.get_actors("car")
        car_base_row = car_rows[2]
        car_mid_row = car_rows[1]
        car_top_row = car_rows[0]
        
        self.check_car_collision(car_base_row, cast, 250)
        self.check_car_collision(car_mid_row, cast, 290)
        self.check_car_collision(car_top_row, cast, 330)
        
            
        
        log_rows = cast.get_actors("log")
        base_row = log_rows[2]
        mid_row = log_rows[1]
        top_row = log_rows[0]
        
        if self._is_game_over:
                
            
            return
            
        else:
                
            chicken = cast.get_first_actor("chicken") 
        
            if chicken.get_position().get_y() == 170:
                self._is_game_over = True
            self.check_log_collision(base_row, cast, 170)
            
            
            if chicken.get_position().get_y() == 130:
                self._is_game_over = True
            self.check_log_collision(mid_row, cast, 130)
            
            
            if chicken.get_position().get_y() == 90:
                self._is_game_over = True
            self.check_log_collision(top_row, cast, 90)
            
        
            
            if self._is_game_over:
                chicken.set_text("+")
                

                
    def check_log_collision(self, row, cast, y):   
        chicken = cast.get_first_actor("chicken")         
        log_list = row.get_logs()
        
        for log in log_list:
            
            if chicken.get_position().get_y() == y and chicken.get_position().get_x() in range(log.get_position().get_x(), log.get_position().get_x()+60):
                chicken.set_position(Point(log.get_position().get_x(), y))
                self._is_game_over = False
                if chicken.get_position().get_x() <= 0:
                    self._is_game_over = True
                    
                 
                
                
    def check_car_collision(self, row, cast, y):   
        chicken = cast.get_first_actor("chicken")         
        car_list = row.get_cars()
        
        for car in car_list:
            
            if chicken.get_position().get_y() == y and chicken.get_position().get_x() in range(car.get_position().get_x() - 20, car.get_position().get_x() + 20):
                self._is_game_over = True 
                chicken.set_text("+")
                  
            
        
                
    def _restart(self, cast, script):
        """When the game is over, this would be the method running in the game loop.
        It takes the cast and script as parameters and renders the white colored cycles without collisions.
        There is an if statement that checks if the user has pressed the spacebar to restart the game.
        
        

        Args:
            cast (_type_): _description_
            script (_type_): _description_
        """
        
        chicken = cast.get_first_actor("chicken")
        
        
        car_rows = cast.get_actors("car")
        for rows in car_rows:
            rows.stop_cars()
            for car in rows.get_cars():
                car.set_color(Color(255, 255, 255))
            
        log_rows = cast.get_actors("log")
        for rows in log_rows:
            rows.stop_logs()
            for log in rows.get_logs():
                log.set_color(Color(255, 255, 255))

    
        #checks for input  
        restart = script.get_last_action("input")       
        if restart.get_restart():
            level = cast.get_first_actor("level")
            level.next_level()
            
            
            
            cast.remove_group("lives")
            
            cast.add_actor("lives", Lives())
            
            
            next_level = 1
            level.set_text(f"Level: {next_level}")
            
            chicken = cast.get_first_actor("chicken")
            chicken.set_position(Point(int(MAX_X/2), int(MAX_Y - 30)))
            chicken.set_text("#")
            
            
        
            cast.remove_group("car")
            cast.remove_group("log")
            #car lane 1
            cast.add_actor("car", Car(1, CAR_LANE_ONE, next_level))
            #car lane 2
            cast.add_actor("car", Car(2, CAR_LANE_TWO, next_level))
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
            
            self._action = HandleRestartAction(self._keyboard_service)
            
            
            self._is_game_over=False

            
        else:    pass    
        
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message including the playere that won the round, also applies scores to the appropriate individuals.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        

        if self._is_game_over:
            
            script.add_action("input", self._action)
            

            
            message = Actor()
            x = int(MAX_X / 2)
            y = int(10)
            position = Point(x, y)
            message.set_position(position)
            
            
            message.set_text("Game Over (Press Spacebar to Start again.)")  
            message.set_font_size = 20
            
            
                
            cast.add_actor("messages", message)                
    
            self._is_game_over = True


    def _handle_life_loss(self, cast, script):
        """Shows the 'game over' message including the playere that won the round, also applies scores to the appropriate individuals.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        

        if self._is_game_over:

            message = Actor()
            x = int(MAX_X / 2)
            y = int(10)
            position = Point(x, y)
            message.set_position(position)
            message.set_font_size = 20
            
            
            
            message.set_text("Your Chicken Lost A Life, Restarting In 2 seconds")  
            
                
            cast.add_actor("messages", message) 
            
            

            
            self._is_game_over = True
            
    def _continue(self, cast, script):
        time.sleep(2)
        message = cast.get_last_actor("messages")
        message.set_text("")
        
        chicken = cast.get_first_actor("chicken")         
        
        chicken.set_text("#")
        
        chicken = cast.get_first_actor("chicken")
        if chicken.get_position().get_y() < 211:
            chicken.set_position(Point(int(MAX_X / 2), 210))
    
        elif chicken.get_position().get_y() < 370:
            chicken.set_position(Point(int(MAX_X/2), int(MAX_Y - 30)))
        self._is_game_over=False
        