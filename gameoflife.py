from random import randint
from typing import List
import time

DEAD = 0
ALIVE = 1


def random_state(width: int, height: int) -> List:
    board = []
    for _ in range(width):
        board.append([randint(0, 1) for _ in range(height)])
    return board


def dead_state(width: int, height: int) -> List:
    return [[DEAD for _ in range(height)] for _ in range(width)]


def render(state):
    """Displays a state by printing it to the terminal.
    Parameters
    ----------
    state: a Game state
    Returns
    -------
    Nothing - this is purely a display function.
    """
    display_as = {
        DEAD: ' ',
        # This is "unicode" for a filled-in square. You can also just use a thick
        # "ASCII" character like a '$' or '#'.
        ALIVE: u"\u2588"
    }
    lines = []
    for y in range(0, len(state[0])):
        line = ''
        for x in range(0, len(state)):
            line += display_as[state[x][y]] * 2
        lines.append(line)
    print("\n".join(lines))


def next_cell_stage(x, y, board):
    alive_neighbor = 0
    for i in range(x-1, x+1+1):
        if i < 0 or i >= len(board) - 1:
            continue
        for j in range(y-1, y+1+1):
            if j < 0 or j >= len(board[0]) - 1:
                continue
            if i == x and j == y:
                continue
            if board[i][j] == ALIVE:
                alive_neighbor += 1

    if board[x][y]:
        if alive_neighbor <= 1:
            return DEAD
        elif alive_neighbor <= 3:
            return ALIVE
        else:
            return DEAD
    else:
        if alive_neighbor == 3:
            return ALIVE
        else:
            return DEAD


def next_board_stage(board):

    next_state = dead_state(len(board), len(board[0]))
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            next_state[i][j] = next_cell_stage(i, j, board)

    return next_state


def run(init_board):
    next_stage = init_board
    while True:
        render(next_stage)
        next_stage = next_board_stage(next_stage)
        time.sleep(0.03)


if __name__ == "__main__":
    init_board = random_state(80, 80)
    run(init_board)
