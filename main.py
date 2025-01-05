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
    drop_chip(3)


if __name__ == '__main__':
    grid = [[0 for _ in range(7)] for _ in range(6)]

    grid[5][0] = 2

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
        print("Player's turn", players_turn)





