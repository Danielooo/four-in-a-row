from array import array

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


def print_grid():
    for row in grid:
        print(row)
    print()


def is_win_condition_met():
    for row in grid:
        if check_four_in_a_row(row):
            return True
    return False


def check_four_in_a_row(row):
    count = 1
    for i in range(1, len(row)):
        if row[i] and row[i] == row[i - 1]:
            count += 1
            if count == 4:
                return True
        else:
            count = 1
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Access the element at row 2, column 3
    # element = grid[2][3]

    grid = [[0 for _ in range(7)] for _ in range(6)]

    # Print the grid
    print_grid()

    # grid[5][0] = 2
    player_input = int(input("Enter your x position (0-6): "))
    player_move(player_input)
    print_grid()
    if is_win_condition_met(): print("Win condition met!")


    player_input = int(input("Enter your x position (0-6): "))
    player_move(player_input)
    print_grid()
    if is_win_condition_met(): print("Win condition met!")

    player_input = int(input("Enter your x position (0-6): "))
    player_move(player_input)
    print_grid()
    if is_win_condition_met(): print("Win condition met!")

    player_input = int(input("Enter your x position (0-6): "))
    player_move(player_input)
    print_grid()
    if is_win_condition_met(): print("Win condition met!")

