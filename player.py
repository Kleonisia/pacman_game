from consts import *
from independent_variables import timer_pacman, counter, level

class Player:
    def __init__(self, i_x, i_y, speed, img, direction, movement, turns, lives):
        self.i_x = i_x
        self.i_y = i_y
        self.speed = speed
        self.img = img
        self.direction = direction
        self.movement = movement
        self.turns = turns
        self.lives = lives

    def move(self):
        self.check_position()
        if timer_pacman != 0:
            return
        if not self.movement:
            return
        match self.direction:
            case 0:
                if self.turns[0]:
                    self.i_x += 1
            case 1:
                if self.turns[1]:
                    self.i_x -= 1
            case 2:
                if self.turns[2]:
                    self.i_y -= 1
            case 3:
                if self.turns[3]:
                    self.i_y += 1

    def check_position(self):
        self.turns = [False, False, False, False]
        # print(i_x, i_y, sep=' ')
        if self.i_x == 29 and self.i_y == 15:
            self.turns[0] = True
        if self.i_x == 0 and self.i_y == 15:
            self.turns[1] = True
            self.i_x, self.i_y = 28, 15
        if level[self.i_y][self.i_x + 1] < 3:
            self.turns[0] = True
        if level[self.i_y][self.i_x - 1] < 3:
            self.turns[1] = True
        if level[self.i_y - 1][self.i_x] < 3:
            self.turns[2] = True
        if level[self.i_y + 1][self.i_x] < 3:
            self.turns[3] = True
        # print(*turns)

    def draw(self):
        player_x, player_y = self.i_x * square_x, self.i_y * square_y
        match self.direction:
            case 0:  # Right
                screen.blit(player_images[counter // 5], (player_x, player_y))
            case 1:  # Left
                screen.blit(pg.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
            case 2:  # Up
                screen.blit(pg.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
            case 3:  # Down
                screen.blit(pg.transform.rotate(player_images[counter // 5], -90), (player_x, player_y))

    def reset(self):
        self.i_x, self.i_y = player_i_x, player_i_y
        self.direction = 0
        self.movement = False
        self.lives -= 1

pacman = Player(player_i_x, player_i_y, pacman_speed, player_images, 0, movement, turns_allowed, lives)
