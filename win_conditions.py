def is_win_condition_met(grid):
    if check_rows(grid) or check_columns(grid) or check_four_in_a_diagonal(grid):
        return True
    return False

def check_rows(grid):
    for row in grid:
        if check_four_in_a_row(row):
            return True
    return False

def check_columns(grid):
    for i in range(7):
        column = [row[i] for row in grid]
        if check_four_in_a_column(column):
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

def check_four_in_a_column(column):
    count = 1
    for i in range(1, len(column)):
        if column[i] and column[i] == column[i - 1]:
            count += 1
            if count == 4:
                return True
        else:
            count = 1
    return False

def check_four_in_a_diagonal(grid):
    for i in range(3):
        for j in range(4):
            if grid[i][j] and grid[i][j] == grid[i + 1][j + 1] == grid[i + 2][j + 2] == grid[i + 3][j + 3]:
                return True
    for i in range(3):
        for j in range(3, 7):
            if grid[i][j] and grid[i][j] == grid[i + 1][j - 1] == grid[i + 2][j - 2] == grid[i + 3][j - 3]:
                return True
    return False