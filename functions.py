from independent_variables import *

def game_win():
    print("You win!")
    print(f'Your score: {score}')
    global running
    running = False

def game_over():
    print("Game Over")
    print(f'Your score: {score}')
    global running
    running = False
    # print(f'runnggging: {running}')