from tkinter import *
import numpy as np

class Tile:
    def __init__(self, is_mine):
        self.adjacents = {}
        self.coords = None
        self.is_mine = is_mine
        self.is_flagged = False
        self.is_revealed = False
        self.value = is_mine * -1
    def __repr__(self):
        return str(self.value)
    def __hash__(self):
        return hash(self.coords)
    
def create_board(dim, n_mines):
    board = np.array([Tile(True)]*n_mines + [Tile(False)]*(dim**2 - n_mines))
    np.random.shuffle(board)
    board = board.reshape((dim, dim))
    for k, v in np.ndenumerate(board):
        v.coords = k
        if v.is_mine:
            v.adjecent = {*board[k[0]-1:k[0]+2, k[1]-1:k[1]+2].flat} - {v}
            print(v.adjecent)
            for adj in v.adjecent:
                if not adj.is_mine:
                    adj.value += 1
    return board




print(create_board(10, 20))


        
