import pathlib

WIDTH = 1280
HEIGHT = 720

FPS = 60

# Char consts
MAX_SPEED = 10
PLAYER_ACC = 1.5
SHOOT_RATE = 250  # interval between shots: milliseconds


class Color:
    white = (255, 255, 255)
    dark_blue = (41, 41, 66)
    dark_yellow = (109, 94, 10)
    red = (255, 0, 0)
    green = (106, 0, 100)
    light_green = (20, 211, 136)
    black = (0, 0, 0)


PATH_PROJECT = pathlib.PurePath(__file__).parent
PATH_SPRITES = pathlib.PurePath(PATH_PROJECT).joinpath('sprites/')
PATH_ASSETS = pathlib.PurePath(PATH_PROJECT).joinpath('assets/')
PATH_IMAGES = pathlib.PurePath(PATH_PROJECT).joinpath('assets/images')
PATH_MENUS = pathlib.PurePath(PATH_PROJECT).joinpath('menus/')

CHARACTER_IMAGE_NAME = "dino-spaceship-scaled.png"
STRUCTURE_IMAGE_NAME = "structure.png"
PROJECTILE_IMAGE_NAME = "shot_0003_Layer-8-scaled.png"
FIGHTER_IMAGE_NAME = "fighter.png"
MINE_IMAGE_NAME = "mine.png"
