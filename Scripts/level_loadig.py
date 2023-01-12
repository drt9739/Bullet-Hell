from Scripts.Classes.block import Block


transform_dictionary = {0: ("air", 0, "air.png"), 1: ("ground", 20, "ground.png")}


def level_load(directory, level, board):
    with open(f'Data/Levels/{directory}/{level}', "r") as level_data:
        level_data = level_data.read().split("\n")
        print(level_data)
        level_table = []
        for i in range(0, len(level_data), 1):
            level_table.append([])
            for j in range(len(level_data[i].split())):
                print(i, j)
                block = Block(board, *transform_dictionary[int(level_data[i].split()[j])])
                block.set_coordinates(j, i)
                level_table[i].append(block)
    print(level_data)
    return level_table