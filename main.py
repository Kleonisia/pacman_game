from ghost import Ghost
from player import Player
from board import boards
from functions import game_win
from consts import *

pg.init()

# specifications 2
pg.display.set_caption("pacman")
# pygame.display.init
timer = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 20)
running = True

score = 0
powerup, power_counter = False, 0
counter = 0
timer_ghost, timer_pacman = 0, 0
level = boards
eaten_ghosts = [False, False, False]

pacman = Player(player_i_x, player_i_y, pacman_speed, player_images, 0, movement, turns_allowed, lives)

blinky = Ghost(blinky_i_x, blinky_i_y, ghost_speed, blinky_img, 0, False, 0, target[0], pacman, level)
pinky = Ghost(pinky_i_x, pinky_i_y, ghost_speed, pinky_img, 3, False, 1, target[1], pacman, level)
clyde = Ghost(clyde_i_x, clyde_i_y, ghost_speed, clyde_img, 1, False, 2, target[2], pacman, level)

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

def count(a, i_x, i_y, p_c, power, e_g): #e_g = eaten_ghosts, p_c = power_counter
    global running
    b = 0
    for i in range(33):
        b += (level[i].count(1) + level[i].count(2))
    if (b == 0):
        running = game_win(score)
        return a, p_c, power, e_g
    if level[i_y][i_x] == 1:
        a += 10
        level[i_y][i_x] = 0
    if level[i_y][i_x] == 2:
        a += 50
        level[i_y][i_x] = 0
        power = True
        p_c = 0
        blinky.img = spooked_img
        pinky.img = spooked_img
        clyde.img = spooked_img
        # do ghost eatable
    return a, p_c, power, e_g


def draw_misc():
    score_text = font.render(f'SCORE: {score}', True, 'white')
    screen.blit(score_text, (10, 825))
    if powerup:
        pg.draw.circle(screen, 'blue', (700, 832), 10)
    lives_text = font.render(f'LIVES: {pacman.lives}', True, 'red')
    screen.blit(lives_text, (300, 825))

def ghosts_move():
    reboot = [False, False, False]
    run = [True, True, True]
    global running, score, eaten_ghosts
    if blinky.img == blinky_img:
        if powerup and not eaten_ghosts[0]: # powerup - True and eaten_ghosts[0] - False
            blinky.img = spooked_img
            score, eaten_ghosts = blinky.reverse_move(timer_ghost, level, score, eaten_ghosts)
        elif not powerup: # powerup - False
            eaten_ghosts[0] = False
            run[0], reboot[0] = blinky.move(timer_ghost, level, score)
            # print(f'ch: {running}, {score}, {timer_ghost}')
        else:
            running = blinky.move(timer_ghost, level, score)
    elif blinky.img == spooked_img:
        if not powerup: # powerup - False
            blinky.img = blinky_img
            run[0], reboot[0] = blinky.move(timer_ghost, level, score)
        if blinky.dead:
            blinky.img = dead_ghost_img
            blinky.dead_move(timer_ghost, level)
        else:
            score, eaten_ghosts = blinky.reverse_move(timer_ghost, level, score, eaten_ghosts)
    else:
        if not powerup: # powerup - False
            eaten_ghosts[0] = False
        if not blinky.dead: #dead - False
            blinky.img = blinky_img
            run[0], reboot[0] = blinky.move(timer_ghost, level, score)
        else:
            blinky.dead_move(timer_ghost, level)
    if pinky.img == pinky_img:
        if powerup and not eaten_ghosts[0]: # powerup - True and eaten_ghosts[0] - False
            pinky.img = spooked_img
            score, eaten_ghosts = pinky.reverse_move(timer_ghost, level, score, eaten_ghosts)
        elif not powerup: # powerup - False
            eaten_ghosts[1] = False
            run[1], reboot[1] = pinky.move(timer_ghost, level, score)
            # print(f'ch: {running}, {score}, {timer_ghost}')
        else:
            run[1], reboot[1] = pinky.move(timer_ghost, level, score)
    elif pinky.img == spooked_img:
        if not powerup: # powerup - False
            pinky.img = pinky_img
            run[1], reboot[1] = pinky.move(timer_ghost, level, score)
        if pinky.dead:
            pinky.img = dead_ghost_img
            pinky.dead_move(timer_ghost, level)
        else:
            score, eaten_ghosts = pinky.reverse_move(timer_ghost, level, score, eaten_ghosts)
    else:
        if not powerup: # powerup - False
            eaten_ghosts[1] = False
        if not pinky.dead: #dead - False
            pinky.img = pinky_img
            run[1], reboot[1] = pinky.move(timer_ghost, level, score)
        else:
            pinky.dead_move(timer_ghost, level)
    if clyde.img == clyde_img:
        if powerup and not eaten_ghosts[0]: # powerup - True and eaten_ghosts[0] - False
            clyde.img = spooked_img
            score, eaten_ghosts = clyde.reverse_move(timer_ghost, level, score, eaten_ghosts)
        elif not powerup: # powerup - False
            eaten_ghosts[2] = False
            run[2], reboot[2] = clyde.move(timer_ghost, level, score)
            # print(f'ch: {running}, {score}, {timer_ghost}')
        else:
            run[2], reboot[2] = clyde.move(timer_ghost, level, score)
    elif clyde.img == spooked_img:
        if not powerup: # powerup - False
            clyde.img = clyde_img
            run[2], reboot[2] = clyde.move(timer_ghost, level, score)
        if clyde.dead:
            clyde.img = dead_ghost_img
            clyde.dead_move(timer_ghost, level)
        else:
            score, eaten_ghosts = clyde.reverse_move(timer_ghost, level, score, eaten_ghosts)
    else:
        if not powerup: # powerup - False
            eaten_ghosts[2] = False
        if not clyde.dead: #dead - False
            clyde.img = clyde_img
            run[2], reboot[2] = clyde.move(timer_ghost, level, score)
        else:
            clyde.dead_move(timer_ghost, level)
    if reboot[0] or reboot[1] or reboot[2]:
        pinky.reset()
        blinky.reset()
        clyde.reset()
    if not (run[0] and run[1] and run[2]):
        running = False

while running:
    # print(pacman.turns[1])
    player_x, player_y = player_i_x * square_x, player_i_y * square_y
    blinky.pac = pacman
    pinky.pac = pacman
    clyde.pac = pacman
    timer.tick(fps)
    if powerup and power_counter < 600:
        power_counter += 1
    elif powerup and power_counter >= 600:
        powerup, power_counter = False, 0
        eaten_ghosts = [False, False, False, False]
    # print(f'check1: {running}')
    ghosts_move()
    # print(f'check2: {running}')
    pacman = blinky.pac

    screen.fill('black')
    draw_board(level)
    draw_misc()
    blinky.draw()
    pinky.draw()
    clyde.draw()
    # print(f'check3: {running}')

    pacman.draw(counter)
    # print(f'check4: {running}')
    pacman.move(timer_pacman, level)
    # print(f'check5: {running}')
    score, power_counter, powerup, eaten_ghosts = count(score, pacman.i_x, pacman.i_y, power_counter, powerup, eaten_ghosts)
    # print(f'check6: {running}')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_RIGHT or event.key == pg.K_d) and pacman.turns[0]:
                pacman.direction = 0
                pacman.movement = True
                # player_i_x += 1
            if (event.key == pg.K_LEFT or event.key == pg.K_a) and pacman.turns[1]:
                pacman.direction = 1
                pacman.movement = True
                # player_i_x -= 1
            if (event.key == pg.K_UP or event.key == pg.K_w) and pacman.turns[2]:
                pacman.direction = 2
                pacman.movement = True
                # player_i_y -= 1
            if (event.key == pg.K_DOWN or event.key == pg.K_s) and pacman.turns[3]:
                pacman.direction = 3
                pacman.movement = True
                # player_i_y += 1
    pg.display.flip()

    if counter < 19:
        counter += 1
    else:
        counter = 0
    if timer_pacman < pacman_speed:
        timer_pacman += 1
    else:
        timer_pacman = 0
    if timer_ghost < ghost_speed:
        timer_ghost += 1
    else:
        timer_ghost = 0
pg.quit()
