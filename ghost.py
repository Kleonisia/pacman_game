from independent_variables import *
from functions import game_over
from player import *
class Ghost:
    def __init__(self, i_x, i_y, speed, img, direction, dead, id, target):
        self.i_x = i_x
        self.i_y = i_y
        self.speed = speed
        self.img = img
        self.direction = direction
        self.dead = dead
        self.id = id
        self.target = target
        self.draw()
        self.check_pos()
    def draw(self):
        screen.blit(self.img, (self.i_x * square_x, self.i_y * square_y))
    def move(self):
        if timer_ghost != 0:
            return
        self.target = (pacman.i_x, pacman.i_y)
        # print(f'Player: {player_i_x} {player_i_y}')
        self.check_pos()
        if self.target[0] > self.i_x and self.target[1] < self.i_y: # 1
            # print('1')
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[3]:
                    self.i_y += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[0] < self.i_x and self.target[1] < self.i_y: # 2
            # print('2')
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        elif self.target[0] < self.i_x and self.target[1] > self.i_y: # 3
            # print('3')
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        elif self.target[0] > self.i_x and self.target[1] > self.i_y: # 4
            # print('4')
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[0] == self.i_x and self.target[1] > self.i_y:
            if self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 1:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 0:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            else:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
        elif self.target[0] == self.i_x and self.target[1] < self.i_y:
            if self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 1:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 0:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            else:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.i_y += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
        elif self.target[1] == self.i_y and self.target[0] > self.i_x:
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 3:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[1] == self.i_y and self.target[0] < self.i_x:
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 2:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.i_x += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        else:
            if pacman.lives == 0:
                game_over()
                return
            self.reset()
            pacman.reset()

    def reverse_move(self):
        if timer_ghost != 0:
            return
        self.target = (pacman.i_x, pacman.i_y)
        self.check_pos()
        if self.target[0] > self.i_x and self.target[1] < self.i_y:
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.i_x += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        elif self.target[0] < self.i_x and self.target[1] < self.i_y:
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[0] < self.i_x and self.target[1] > self.i_y:
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[0] > self.i_x and self.target[1] > self.i_y:
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        elif self.target[0] == self.i_x and self.target[1] > self.i_y:
            if self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 1:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 0:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            else:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
        elif self.target[0] == self.i_x and self.target[1] < self.i_y:
            if self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 1:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 0:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            else:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
        elif self.target[1] == self.i_y and self.target[0] > self.i_x:
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 2:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[1] == self.i_y and self.target[0] < self.i_x:
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 2:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        else:
            self.dead = True
            global eaten_ghosts, score
            eaten_ghosts[self.id] = True
            score += 100

    def dead_move(self):
        if timer_ghost != 0:
            return
        self.target = (blinky_i_x, blinky_i_y)
        # print(f'Player: {player_i_x} {player_i_y}')
        self.check_pos()
        if self.target[0] > self.i_x and self.target[1] < self.i_y: # 1
            # print('1')
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[3]:
                    self.i_y += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[0] < self.i_x and self.target[1] < self.i_y: # 2
            # print('2')
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        elif self.target[0] < self.i_x and self.target[1] > self.i_y: # 3
            # print('3')
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        elif self.target[0] > self.i_x and self.target[1] > self.i_y: # 4
            # print('4')
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[0] == self.i_x and self.target[1] > self.i_y:
            if self.direction == 3:
                if self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 1:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 0:
                if self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            else:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
        elif self.target[0] == self.i_x and self.target[1] < self.i_y:
            if self.direction == 2:
                if self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 1:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[1]:
                    self.i_x -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 0:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            else:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.i_y += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
        elif self.target[1] == self.i_y and self.target[0] > self.i_x:
            if self.direction == 0:
                if self.turns[0]:
                    self.i_x += 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                else:
                    self.direction = 1
                    self.i_x -= 1
            elif self.direction == 3:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            elif self.direction == 2:
                if self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                else:
                    self.direction = 3
                    self.i_y += 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[1]:
                    self.i_x -= 1
                else:
                    self.direction = 0
                    self.i_x += 1
        elif self.target[1] == self.i_y and self.target[0] < self.i_x:
            if self.direction == 1:
                if self.turns[1]:
                    self.i_x -= 1
                elif self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                else:
                    self.direction = 0
                    self.i_x += 1
            elif self.direction == 2:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[2]:
                    self.i_y -= 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 3
                    self.i_y += 1
            elif self.direction == 3:
                if self.turns[1]:
                    self.direction = 1
                    self.i_x -= 1
                elif self.turns[3]:
                    self.i_y += 1
                elif self.turns[0]:
                    self.direction = 0
                    self.i_x += 1
                else:
                    self.direction = 2
                    self.i_y -= 1
            else:
                if self.turns[2]:
                    self.direction = 2
                    self.i_y -= 1
                elif self.turns[3]:
                    self.direction = 3
                    self.i_y += 1
                elif self.turns[0]:
                    self.i_x += 1
                else:
                    self.direction = 1
                    self.i_x -= 1
        else:
            self.dead = False

    def check_pos(self):
        self.turns = [False, False, False, False]
        # print(f'blinky: {self.i_x} {self.i_y}')
        if self.i_x == 29 and self.i_y == 15:
            self.turns[0] = True
            self.i_x = 1
            self.i_y = 15
        if self.i_x == 0 and self.i_y == 15:
            self.turns[1] = True
            self.i_x = 28
            self.i_y = 15
        if level[self.i_y][self.i_x + 1] < 3:
            self.turns[0] = True
        if level[self.i_y][self.i_x - 1] < 3:
            self.turns[1] = True
        if level[self.i_y - 1][self.i_x] < 3:
            self.turns[2] = True
        if level[self.i_y + 1][self.i_x] < 3:
            self.turns[3] = True
        # print(*turns)

    def reset(self):
        if self.id == 0:
            self.i_x, self.i_y = blinky_i_x, blinky_i_y
        elif self.id == 1:
            self.i_x, self.i_y = pinky_i_x, pinky_i_y
        elif self.id == 2:
            self.i_x, self.i_y = clyde_i_x, clyde_i_y

