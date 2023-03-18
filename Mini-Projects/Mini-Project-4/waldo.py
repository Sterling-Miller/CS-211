"""Mini-Project: Wheres Waldo
Sterling Miller, 2023-01-30, CIS 211
"""
Waldo = 'w'
Other = '.'


# For all, There exists at least one:
def all_row_exists_waldo(board: list[list]):
    """ For all rows in the matrix, Waldo is in some column """
    for row in board:
        if Waldo not in row:
            return False
    return True


def all_col_exists_waldo(board):
    """ For all columns in the matrix, Waldo is in some row """
    if len(board) > 0:
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] == Waldo:
                    break
                if row == (len(board) - 1):
                    return False
    return True


# For all, For all:
def all_row_all_waldo(board: list[list]) -> bool:
    """ For all rows in the matrix, Waldo is in every column """
    for row in board:
        if Other in row:
            return False
    return True


def all_col_all_waldo(board: list[list]):
    """ For all the columns in the matrix, Waldo is in every row """
    if len(board) > 0:
        for col in range(len(board[0])):
            if Other in board[col]:
                return False
    return True


# There exists at least one, For all:
def exists_row_all_waldo(board: list[list]):
    """ There is some row in the matrix in which Waldo is in every column """
    for row in board:
        if Other in row:
            pass
        else:
            return True
    return False


def exists_col_all_waldo(board: list[list]):
    """ There is some column in the matrix in which Waldo is in every row """
    if len(board) > 0:
        for col in range(len(board[0])):
            for row in range(len(board)):
                if board[row][col] == Other:
                    break
                elif row == (len(board) - 1):
                    return True
    return False


# There exists, there exists:
def exists_row_exists_waldo(board: list[list]):
    """ There is some row in the matrix in which Waldo is in some column """
    for row in board:
        if Waldo in row:
            return True
    return False


def exists_col_exists_waldo(board: list[list]):
    """ There is some column in the matrix in which Waldo is in some row """
    for row in board:
        for col in row:
            if col == Waldo:
                return True
    return False
