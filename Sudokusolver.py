import numpy as np
from pprint import pprint
sudoku_grid = [
                [0,1,3,0,0,7,0,0,6],
                [0,0,0,0,0,0,0,2,4],
                [0,5,0,8,0,0,0,7,0],
                [0,0,0,9,0,8,7,0,0],
                [0,0,0,0,0,0,0,5,0],
                [0,0,0,6,7,0,0,0,0],
                [0,0,0,0,0,0,9,0,2],
                [7,0,6,0,3,0,8,0,0],
                [0,0,1,0,2,0,0,0,0]
               ]

def possible(x, y, n):
    global sudoku_grid
    for i in range(0,9):
        if sudoku_grid[y][i] == n:
            return False
    for i in range(0,9):
        if sudoku_grid[x][i] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global sudoku_grid
    for y in range(9):
        for x in range(9):
            if sudoku_grid[y][x] == 0:
                for n in range(1,10):
                    if possible(x, y, n):
                        sudoku_grid[y][x] = n
                        solve()
                        sudoku_grid[y][x] = 0
    print(np.matrix(sudoku_grid))
    input("More?")

solve()