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
level = boards # boards[??]


# specifications 2
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("pacman")
# pygame.display.init
timer = pg.time.Clock()
fps = 60
font = pg.font.Font('freesansbold.ttf', 20)


# Player, надо создать класс
player_images = []
player_i_x, player_i_y =  15, 24
player_x, player_y = player_i_x * square_x, player_i_y * square_y # переписать в класс Player
direction = 0
counter = 0
speed = 5
turns_allowed = [False, False, False, False] # R, L, U, D
for i in range(1, 5):
    player_images.append(pg.transform.scale(pg.image.load(f'objects/player_images/{i}.xcf'), (30, 30)))


def draw_board(lvl):
    num1, num2 = square_y, square_x
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            match lvl[i][j]:
                case 1:
                    pg.draw.circle(screen, 'white', ((j + 0.5) * num2, (i + 0.5) * num1), 4)
                case 2:
                    pg.draw.circle(screen, 'white', ((j + 0.5) * num2, (i + 0.5) * num1), 8)
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
    print(i_x, i_y, sep=' ')
    if level[i_y][i_x + 1] < 3:
        turns[0] = True
    if level[i_y][i_x - 1] < 3:
        turns[1] = True
    if level[i_y - 1][i_x] < 3:
        turns[2] = True
    if level[i_y + 1][i_x] < 3:
        turns[3] = True
    print(*turns)
    return turns

running = True
while running:
    player_x, player_y = player_i_x * square_x, player_i_y * square_y
    # print(counter)
    timer.tick(fps)
    screen.fill('black')
    draw_board(level)
    draw_player()
    '''center_x = player_x + 15
    center_y = player_y + 15
    # pg.draw.circle(screen, 'black', (center_x, center_y), 2)'''
    turns_allowed = check_position(player_i_x, player_i_y)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_RIGHT or event.key == pg.K_d) and turns_allowed[0]:
                direction = 0
                player_i_x += 1
            if (event.key == pg.K_LEFT or event.key == pg.K_a) and turns_allowed[1]:
                direction = 1
                player_i_x -= 1
            if (event.key == pg.K_UP or event.key == pg.K_w) and turns_allowed[2]:
                direction = 2
                player_i_y -= 1
            if (event.key == pg.K_DOWN or event.key == pg.K_s) and turns_allowed[3]:
                direction = 3
                player_i_y += 1
    pg.display.flip()
    if counter < 19:
        counter += 1
    else:
        counter = 0
pg.quit()
