
player_sign = 1
computer_sign = 2


def player_move(pos_x):
    drop_chip(pos_x)


def drop_chip(pos_x):
    pos_y = get_lowest_empty_y(pos_x)
    grid[pos_y][pos_x] = player_sign


def get_lowest_empty_y(pos_x):
    for pos_y in range(5, -1, -1):
        if grid[pos_y][pos_x] == 0:
            return pos_y


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Access the element at row 2, column 3
    # element = grid[2][3]

    grid = [[0 for _ in range(7)] for _ in range(6)]

    # Print the grid
    for row in grid:
        print(row)

    print()

    grid[5][0] = 1

    player_move(0)

    for row in grid:
        print(row)
