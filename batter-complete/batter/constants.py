from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Chicken"
FRAME_RATE = 20

# SCREEN
COLUMNS = 20
ROWS = 20
MAX_X = 700
MAX_Y = 1000
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 1000
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "batter/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "batter/assets/sounds/boing.wav"
WELCOME_SOUND = "batter/assets/sounds/start.wav"
OVER_SOUND = "batter/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(90, 168, 0)
BLUE = Color(0, 191, 255)
GREY = Color(155, 155, 155)
LIME = Color(0, 158, 47)
MIDNIGHT_BLUE = Color(25, 25, 112)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "batter/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

CAR_LANE_ONE = 820
CAR_LANE_TWO = 740
CAR_LANE_THREE = 660
CAR_LANE_FOUR = 580
FOX_LANE_ONE = 500
LOG_LANE_ONE = 420
LOG_LANE_TWO = 340
LOG_LANE_THREE = 260
LOG_LANE_FOUR = 180
FOX_LANE_TWO = 100

# CHICKEN
CHICKEN_GROUP = "chickens"
CHICKEN_IMAGES = [f"batter/assets/images/{n:03}.png" for n in range(100, 103)]
CHICKEN_WIDTH = 32
CHICKEN_HEIGHT = 32
CHICKEN_RATE = 6
CHICKEN_VELOCITY = 7

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    # "b": [f"batter/assets/images/{i:03}.png" for i in range(10,19)],
    "b": [f"batter/assets/images/{i:03}.png" for i in range(50,59)],
    "g": [f"batter/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"batter/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"batter/assets/images/{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 40
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 0

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
