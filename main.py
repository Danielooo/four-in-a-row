from array import array
from win_conditions import is_win_condition_met

player_sign = 1
computer_sign = 2
players_turn = True

def player_move(pos_x):
    drop_chip(pos_x)

def drop_chip(pos_x):
    pos_y = get_lowest_empty_y(pos_x)
    grid[pos_y][pos_x] = player_sign if players_turn else computer_sign

def get_lowest_empty_y(pos_x):
    for pos_y in range(5, -1, -1):
        if grid[pos_y][pos_x] == 0:
            return pos_y

def print_grid():
    for row in grid:
        print(row)
    print()


def computer_move():
    check_three_blockable()
    drop_chip(5)
    pass



def check_three_blockable():
    result = check_three_in_a_row(grid, player_sign)
    if result:
        y, x = result
    print("Result", result)
    if result:
        print("possible win at", result)
        if possible_block_left(result):
            print("Block left")
            print(is_bottom_or_chip_below(y, x - 3))
            if is_bottom_or_chip_below(y, x - 3):

                print(y, x - 3)
                print("doable")
                drop_chip(x-3)
        elif possible_block_right(result):
            return (x, y + 1)
        else: 
            print("No block possible")
            return False



def is_bottom_or_chip_below(y, x):
    print(y, x)
    print(y + 1 < 6)
    if y == len(grid) - 1:
        return True
    elif grid[y + 1][x] != 0:
        return True
    else:
        return False



def possible_block_left(result):
    y, x = result
    if x - 3 < 0:
        return False
    if grid[y][x - 3] == 0:
        return True
    else:
        return False
    

def possible_block_right(result):
    y, x = result
    if x + 1 > 6:
        return False
    if grid[result[0]][result[1] + 1] == 0:
        return True
    else:
        return False


def check_three_in_a_row(grid, player_sign):
    for y in range(len(grid)):
        count = 0  # Reset count at the start of each row
        for x in range(len(grid[y])):
            if grid[y][x] == player_sign:
                count += 1
                print("Count", count)
                if count == 3:
                    return (y, x)
            else:
                count = 0  # Reset count when a non-matching cell is encountered
    return False


if __name__ == '__main__':
    grid = [[0 for _ in range(7)] for _ in range(6)]

    # grid[5][0] = 2

    print_grid()

    while(True):
        if players_turn:
            player_input = int(input("Enter your x position (0-6): "))
            player_move(player_input)
            
        else:
            computer_move()
        
        print_grid()
        if is_win_condition_met(grid): 
            print("Win condition met!") 
            break

        players_turn = not players_turn





