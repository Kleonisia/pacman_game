from board import boards
import pygame as pg
import math

pg.init()

PI = math.pi

# specifications 1
WIDTH = 800
HEIGHT = 850
square_x = (WIDTH // 30)
square_y = ((HEIGHT - 50) // 32)
level = boards  # boards[??]

# specifications 2
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("pacman")
# pygame.display.init
timer = pg.time.Clock()
fps = 60
font = pg.font.Font('freesansbold.ttf', 20)
score = 0
powerup, power_counter, eaten_ghosts = False, 0, [False, False, False, False]

# Player, надо создать класс
player_images = []
player_i_x, player_i_y = 15, 24
player_x, player_y = player_i_x * square_x, player_i_y * square_y  # переписать в класс Player
direction = 0
counter = 0
c = 0  # controls movement of pacman
speed = 5
lives = 3
movement = False
turns_allowed = [False, False, False, False]  # R, L, U, D
for i in range(1, 5):
    player_images.append(pg.transform.scale(pg.image.load(f'objects/player_images/{i}.xcf'), (30, 30)))


# Ghosts
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
    def draw(self):
        screen.blit(self.img, (self.i_x * square_x, self.i_y * square_y))

ghost_speed = 3
blinky_i_x, blinky_i_y = 14, 12
pinky_i_x, pinky_i_y = 14, 15
inky_i_x, inky_i_y = 12, 15
clyde_i_x, clyde_i_y = 16, 15
blinky_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/blinky.png'), (30, 30))
pinky_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/pinky.xcf'), (30, 30))
inky_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/inky.xcf'), (30, 30))
clyde_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/clyde.xcf'), (30, 30))
spooked_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/powerup.xcf'), (30, 30))
dead_ghost_img = pg.transform.scale(pg.image.load(f'objects/ghosts_images/dead.png'), (30, 30))
target = [(player_x, player_y), (player_x, player_y), (player_x, player_y), (player_x, player_y)]

blinky = Ghost(blinky_i_x, blinky_i_y, ghost_speed, blinky_img, 0, False, 0, target[0])
pinky = Ghost(pinky_i_x, pinky_i_y, ghost_speed, pinky_img, 2, False, 0, target[1])
inky = Ghost(inky_i_x, inky_i_y, ghost_speed, inky_img, 2, False, 0, target[2])
clyde = Ghost(clyde_i_x, clyde_i_y, ghost_speed, clyde_img, 2, False, 0, target[3])

def draw_board(lvl):
    num1, num2 = square_y, square_x
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            match lvl[i][j]:
                case 1:
                    pg.draw.circle(screen, 'white', ((j + 0.5) * num2, (i + 0.5) * num1), 4)
                case 2:
                    pg.draw.circle(screen, 'yellow', ((j + 0.5) * num2, (i + 0.5) * num1), 10)
                case 3:
                    pg.draw.line(screen, 'blue', ((j + 0.5) * num2, i * num1),
                                 ((j + 0.5) * num2, (i + 1) * num1), 3)
                case 4:
                    pg.draw.line(screen, 'blue', (j * num2, (i + 0.5) * num1),
                                 ((j + 1) * num2, (i + 0.5) * num1), 3)
                case 5:
                    pg.draw.arc(screen, 'blue', [(j - 0.5) * num2, (i + 0.5) * num1, num2, num1], 0, PI / 2, 3)
                case 6:
                    pg.draw.arc(screen, 'blue', [(j + 0.5) * num2, (i + 0.5) * num1, num2, num1], PI / 2, PI, 3)
                case 7:
                    pg.draw.arc(screen, 'blue', [(j + 0.5) * num2, (i - 0.5) * num1, num2, num1 + 1], PI, 3 * PI / 2, 3)
                case 8:
                    pg.draw.arc(screen, 'blue', [(j - 0.5) * num2, (i - 0.5) * num1, num2 + 2, num1 + 1], 3 * PI / 2, 0,
                                3)
                case 9:
                    pg.draw.line(screen, 'white', (j * num2, (i + 0.5) * num1),
                                 ((j + 1) * num2, (i + 0.5) * num1), 3)


def draw_player():
    match direction:
        case 0:  # Right
            screen.blit(player_images[counter // 5], (player_x, player_y))
        case 1:  # Left
            screen.blit(pg.transform.flip(player_images[counter // 5], True, False), (player_x, player_y))
        case 2:  # Up
            screen.blit(pg.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
        case 3:  # Down
            screen.blit(pg.transform.rotate(player_images[counter // 5], -90), (player_x, player_y))


def check_position(i_x, i_y):
    turns = [False, False, False, False]
    # print(i_x, i_y, sep=' ')
    if i_x == 29 and i_y == 15:
        turns[0] = True
        return 1, 15, turns
    if i_x == 0 and i_y == 15:
        turns[1] = True
        return 28, 15, turns
    if level[i_y][i_x + 1] < 3:
        turns[0] = True
    if level[i_y][i_x - 1] < 3:
        turns[1] = True
    if level[i_y - 1][i_x] < 3:
        turns[2] = True
    if level[i_y + 1][i_x] < 3:
        turns[3] = True
    # print(*turns)
    return i_x, i_y, turns


def move(d, i_x, i_y, f, turns):
    if c != 0:
        return i_x, i_y
    if not f:
        return i_x, i_y
    match d:
        case 0:
            if turns[0]:
                i_x += 1
        case 1:
            if turns[1]:
                i_x -= 1
        case 2:
            if turns[2]:
                i_y -= 1
        case 3:
            if turns[3]:
                i_y += 1
    return i_x, i_y


def count(a, i_x, i_y, power, p_c, e_g):
    if level[i_y][i_x] == 1:
        a += 10
        level[i_y][i_x] = 0
    if level[i_y][i_x] == 2:
        a += 50
        level[i_y][i_x] = 0
        power = True
        p_c = 0
        e_g = [False, False, False, False]
        blinky.img = spooked_img
        pinky.img = spooked_img
        inky.img = spooked_img
        clyde.img = spooked_img
        # do ghost eatable
    return a, power, p_c, e_g


def draw_misc():
    score_text = font.render(f'SCORE: {score}', True, 'white')
    screen.blit(score_text, (10, 825))
    if powerup:
        pg.draw.circle(screen, 'blue', (700, 832), 10)
    lives_text = font.render(f'LIVES: {lives}', True, 'red')
    screen.blit(lives_text, (300, 825))


running = True
while running:
    player_x, player_y = player_i_x * square_x, player_i_y * square_y
    # print(counter)
    timer.tick(fps)
    if powerup and power_counter < 600:
        power_counter += 1
    elif powerup and power_counter >= 600:
        powerup, power_counter, eaten_ghosts = False, 0, [False, False, False, False]
        blinky.img = blinky_img
        pinky.img = pinky_img
        inky.img = inky_img
        clyde.img = clyde_img
    screen.fill('black')
    draw_board(level)
    draw_player()
    player_i_x, player_i_y, turns_allowed = check_position(player_i_x, player_i_y)
    player_i_x, player_i_y = move(direction, player_i_x, player_i_y, movement, turns_allowed)
    score, powerup, power_counter, eaten_ghosts = count(score, player_i_x, player_i_y, powerup, power_counter,
                                                        eaten_ghosts)
    draw_misc()
    blinky.draw()
    pinky.draw()
    inky.draw()
    clyde.draw()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_RIGHT or event.key == pg.K_d) and turns_allowed[0]:
                direction = 0
                movement = True
                # player_i_x += 1
            if (event.key == pg.K_LEFT or event.key == pg.K_a) and turns_allowed[1]:
                direction = 1
                movement = True
                # player_i_x -= 1
            if (event.key == pg.K_UP or event.key == pg.K_w) and turns_allowed[2]:
                direction = 2
                movement = True
                # player_i_y -= 1
            if (event.key == pg.K_DOWN or event.key == pg.K_s) and turns_allowed[3]:
                direction = 3
                movement = True
                # player_i_y += 1
    pg.display.flip()
    if counter < 19:
        counter += 1
    else:
        counter = 0
    if c < 9:
        c += 1
    else:
        c = 0
pg.quit()
