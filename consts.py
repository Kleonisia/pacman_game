import pygame as pg
from math import pi


PI = pi

# specifications 1
WIDTH = 800
HEIGHT = 850
square_x = (WIDTH // 30)
square_y = ((HEIGHT - 50) // 32)  # boards[??]
fps = 60

screen = pg.display.set_mode([WIDTH, HEIGHT])

# Player consts
player_images = []
player_i_x, player_i_y = 15, 24
player_x, player_y = player_i_x * square_x, player_i_y * square_y
direction = 0
pacman_speed = 5
lives = 3
movement = False
turns_allowed = [False, False, False, False]  # R, L, U, D
for i in range(1, 5):
    player_images.append(pg.transform.scale(pg.image.load(f'objects/player_images/{i}.xcf'), (30, 30)))

# const Ghosts
ghost_speed = 9
blinky_i_x, blinky_i_y = 14, 12
pinky_i_x, pinky_i_y = 2, 2
clyde_i_x, clyde_i_y = 27, 30
blinky_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/blinky.png'), (30, 30))
pinky_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/pinky.xcf'), (30, 30))
clyde_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/clyde.xcf'), (30, 30))
spooked_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/powerup.xcf'), (30, 30))
dead_ghost_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/dead.png'), (30, 30))
target = [(player_i_x, player_i_y), (player_i_x, player_i_y), (player_i_x, player_i_y)]
