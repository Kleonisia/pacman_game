from functions import *
from consts import *

# timer_ghost, level
class Ghost:
    def __init__(self, i_x, i_y, speed, img, direction, dead, id, target, pacman, level):
        self.i_x = i_x
        self.i_y = i_y
        self.speed = speed
        self.img = img
        self.direction = direction
        self.dead = dead
        self.id = id
        self.target = target
        self.pac = pacman
        self.draw()
        self.check_pos(level)

    def __set(self):
        if self.id == 0:
            self.Blinky_i_x, self.Blinky_i_y = self.i_x, self.i_y
        elif self.id == 1:
            self.Pinky_i_x, self.Pinky_i_y = self.i_x, self.i_y
        else:
            self.Clyde_i_x, self.Clyde_i_y = self.i_x, self.i_y
    def __f_move(self, p0, p1, p2, p3):
        a = [p0, p1, p2, p3]
        b = [[0, 0], [0, 0], [0, 0], [0, 0]]
        for i in range(len(a)):
            match a[i]:
                case 0:
                    b[i][0], b[i][1] = 1, 0
                case 1:
                    b[i][0], b[i][1] = -1, 0
                case 2:
                    b[i][0], b[i][1] = 0, -1
                case 3:
                    b[i][0], b[i][1] = 0, 1
        if self.turns[p0]:
            self.direction = p0
            self.i_x, self.i_y = self.i_x + b[0][0], self.i_y + b[0][1]
        elif self.turns[p1]:
            self.direction = p1
            self.i_x, self.i_y = self.i_x + b[1][0], self.i_y + b[1][1]
        elif self.turns[p2]:
            self.direction = p2
            self.i_x, self.i_y = self.i_x + b[2][0], self.i_y + b[2][1]
        else:
            self.direction = p3
            self.i_x, self.i_y = self.i_x + b[3][0], self.i_y + b[3][1]
    def draw(self):
        screen.blit(self.img, (self.i_x * square_x, self.i_y * square_y))
    def move(self, timer_ghost, level, score):
        res1, res2 = True, False
        if timer_ghost != 0:
            return res1, res2
        self.target = (self.pac.i_x, self.pac.i_y)
        self.check_pos(level)
        if self.target[0] > self.i_x and self.target[1] < self.i_y: # 1
            if self.direction == 0:
                self.__f_move(0, 2, 3, 1)
            elif self.direction == 2:
                self.__f_move(2, 0, 1, 3)
            elif self.direction == 3:
                self.__f_move(0, 1, 3, 2)
            else:
                self.__f_move(2, 1, 3, 0)
            self.__set()
        elif self.target[0] < self.i_x and self.target[1] < self.i_y: # 2
            if self.direction == 1:
                self.__f_move(1, 2, 3, 0)
            elif self.direction == 2:
                self.__f_move(2, 1, 0, 3)
            elif self.direction == 3:
                self.__f_move(1, 0, 3, 2)
            else:
                self.__f_move(2, 0, 3, 1)
            self.__set()
        elif self.target[0] < self.i_x and self.target[1] > self.i_y: # 3
            if self.direction == 1:
                self.__f_move(1, 3, 2, 0)
            elif self.direction == 3:
                self.__f_move(3, 1, 0, 2)
            elif self.direction == 2:
                self.__f_move(1, 0, 2, 3)
            else:
                self.__f_move(3, 0, 2, 1)
            self.__set()
        elif self.target[0] > self.i_x and self.target[1] > self.i_y: # 4
            if self.direction == 0:
                self.__f_move(0, 3, 2, 1)
            elif self.direction == 3:
                self.__f_move(3, 0, 1, 2)
            elif self.direction == 2:
                self.__f_move(0, 2, 1, 3)
            else:
                self.__f_move(3, 1, 2, 0)
            self.__set()
        elif self.target[0] == self.i_x and self.target[1] > self.i_y:
            if self.direction == 3:
                self.__f_move(3, 0, 1, 2)
            elif self.direction == 1:
                self.__f_move(3, 1, 2, 0)
            elif self.direction == 0:
                self.__f_move(3, 0, 2, 1)
            else:
                self.__f_move(1, 0, 2, 3)
            self.__set()
        elif self.target[0] == self.i_x and self.target[1] < self.i_y:
            if self.direction == 2:
                self.__f_move(2, 0, 1, 3)
            elif self.direction == 1:
                self.__f_move(2, 1, 3, 0)
            elif self.direction == 0:
                self.__f_move(2, 0, 3, 1)
            else:
                self.__f_move(1, 0, 3, 2)
            self.__set()
        elif self.target[1] == self.i_y and self.target[0] > self.i_x:
            if self.direction == 0:
                self.__f_move(0, 3, 2, 1)
            elif self.direction == 3:
                self.__f_move(0, 3, 1, 2)
            elif self.direction == 2:
                self.__f_move(0, 2, 1, 3)
            else:
                self.__f_move(2, 3, 1, 0)
            self.__set()
        elif self.target[1] == self.i_y and self.target[0] < self.i_x:
            if self.direction == 1:
                self.__f_move(1, 2, 3, 0)
            elif self.direction == 2:
                self.__f_move(1, 2, 0, 3)
            elif self.direction == 3:
                self.__f_move(1, 3, 0, 2)
            else:
                self.__f_move(2, 3, 0, 1)
            self.__set()
        else:
            res2 = True
            if self.pac.lives <= 0:
                res1 = game_over(score)
            self.pac.reset()
        return res1, res2
    def reverse_move(self, timer_ghost, level, score, eaten_ghosts):
        if timer_ghost != 0:
            return score, eaten_ghosts
        self.target = (self.pac.i_x, self.pac.i_y)
        self.check_pos(level)
        if self.target[0] > self.i_x and self.target[1] < self.i_y:
            if self.direction == 1:
                self.__f_move(1, 3, 2, 0)
            elif self.direction == 3:
                self.__f_move(3, 1, 0, 2)
            elif self.direction == 2:
                self.__f_move(1, 2, 0, 3)
            else:
                self.__f_move(3, 2, 0, 1)
        elif self.target[0] < self.i_x and self.target[1] < self.i_y:
            if self.direction == 0:
                self.__f_move(0, 3, 2, 1)
            elif self.direction == 3:
                self.__f_move(3, 0, 1, 2)
            elif self.direction == 2:
                self.__f_move(0, 2, 1, 3)
            else:
                self.__f_move(3, 1, 2, 0)
        elif self.target[0] < self.i_x and self.target[1] > self.i_y:
            if self.direction == 0:
                self.__f_move(0, 2, 3, 1)
            elif self.direction == 2:
                self.__f_move(2, 0, 1, 3)
            elif self.direction == 3:
                self.__f_move(0, 3, 1, 2)
            else:
                self.__f_move(2, 1, 3, 0)
        elif self.target[0] > self.i_x and self.target[1] > self.i_y:
            if self.direction == 1:
                self.__f_move(1, 2, 3, 0)
            elif self.direction == 2:
                self.__f_move(2, 1, 0, 3)
            elif self.direction == 3:
                self.__f_move(1, 3, 0, 2)
            else:
                self.__f_move(2, 0, 3, 1)
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
                self.__f_move(3, 1, 0, 2)
            elif self.direction == 1:
                self.__f_move(3, 1, 2, 0)
            elif self.direction == 0:
                self.__f_move(3, 0, 2, 1)
            else:
                self.__f_move(1, 0, 3, 2)
        elif self.target[1] == self.i_y and self.target[0] > self.i_x:
            if self.direction == 1:
                self.__f_move(1, 2, 3, 0)
            elif self.direction == 2:
                self.__f_move(1, 2, 0, 3)
            elif self.direction == 3:
                self.__f_move(1, 3, 0, 2)
            else:
                self.__f_move(2, 3, 1, 0)
        elif self.target[1] == self.i_y and self.target[0] < self.i_x:
            if self.direction == 0:
                self.__f_move(0, 2, 3, 1)
            elif self.direction == 2:
                self.__f_move(0, 2, 1, 3)
            elif self.direction == 3:
                self.__f_move(0, 3, 1, 2)
            else:
                self.__f_move(2, 3, 1, 0)
        else:
            self.dead = True
            # исправить
            eaten_ghosts[self.id] = True
            score += 100
        return score, eaten_ghosts

    def dead_move(self, timer_ghost, level):
        if timer_ghost != 0:
            return
        self.target = (blinky_i_x, blinky_i_y)
        self.check_pos(level)
        if self.target[0] > self.i_x and self.target[1] < self.i_y: # 1
            if self.direction == 0:
                self.__f_move(0, 2, 3, 1)
            elif self.direction == 2:
                self.__f_move(2, 0, 1, 3)
            elif self.direction == 3:
                self.__f_move(0, 1, 3, 2)
            else:
                self.__f_move(2, 1, 3, 0)
        elif self.target[0] < self.i_x and self.target[1] < self.i_y: # 2
            if self.direction == 1:
                self.__f_move(1, 2, 3, 0)
            elif self.direction == 2:
                self.__f_move(2, 1, 0, 3)
            elif self.direction == 3:
                self.__f_move(1, 0, 3, 2)
            else:
                self.__f_move(2, 0, 3, 1)
        elif self.target[0] < self.i_x and self.target[1] > self.i_y: # 3
            if self.direction == 1:
                self.__f_move(1, 3, 2, 0)
            elif self.direction == 3:
                self.__f_move(3, 1, 0, 2)
            elif self.direction == 2:
                self.__f_move(1, 0, 2, 3)
            else:
                self.__f_move(3, 0, 2, 1)
        elif self.target[0] > self.i_x and self.target[1] > self.i_y: # 4
            if self.direction == 0:
                self.__f_move(0, 3, 2, 1)
            elif self.direction == 3:
                self.__f_move(3, 0, 1, 2)
            elif self.direction == 2:
                self.__f_move(0, 2, 1, 3)
            else:
                self.__f_move(3, 1, 2, 0)
        elif self.target[0] == self.i_x and self.target[1] > self.i_y:
            if self.direction == 3:
                self.__f_move(3, 0, 1, 2)
            elif self.direction == 1:
                self.__f_move(3, 1, 2, 0)
            elif self.direction == 0:
                self.__f_move(3, 0, 2, 1)
            else:
                self.__f_move(1, 0, 2, 3)
        elif self.target[0] == self.i_x and self.target[1] < self.i_y:
            if self.direction == 2:
                self.__f_move(2, 0, 1, 3)
            elif self.direction == 1:
                self.__f_move(2, 1, 3, 0)
            elif self.direction == 0:
                self.__f_move(2, 0, 3, 1)
            else:
                self.__f_move(1, 0, 3, 2)
        elif self.target[1] == self.i_y and self.target[0] > self.i_x:
            if self.direction == 0:
                self.__f_move(0, 3, 2, 1)
            elif self.direction == 3:
                self.__f_move(0, 3, 1, 2)
            elif self.direction == 2:
                self.__f_move(0, 2, 1, 3)
            else:
                self.__f_move(2, 3, 1, 0)
        elif self.target[1] == self.i_y and self.target[0] < self.i_x:
            if self.direction == 1:
                self.__f_move(1, 2, 3, 0)
            elif self.direction == 2:
                self.__f_move(1, 2, 0, 3)
            elif self.direction == 3:
                self.__f_move(1, 3, 0, 2)
            else:
                self.__f_move(2, 3, 0, 1)
        else:
            self.dead = False

    def check_pos(self, level):
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
        else:
            self.i_x, self.i_y = clyde_i_x, clyde_i_y

