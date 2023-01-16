import os

from Scripts.Class.block import Block
from config import level_path


def load_level(file: str, board: object) -> list:
    path = os.path.abspath('data\\' + file)
    result, res = [], []

    with open(path) as file:
        level = file.readlines()

    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == '0':
                res.append(0)
            elif level[i][j] == 'b':
                res.append(Block(board, 'ground', 20, 'ground.png', j, i))
        result.append(res)
        res.clear()

    return result