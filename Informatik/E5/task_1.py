from random import randint

# ===== Please do not modify this section ======
"""
' ': Water (empty space)
'O': placed ship, still floating
'X': sunk ship!
'-': missed shots (the user tried these coordinates but no ship was there)
"""
NUMBER_OF_SHIPS = 5
BOARD_SIZE = 5
WATER = ' '
SHIP = 'O'
SUNK_SHIP = 'X'
MISSED_SHOT = '-'


# ==============================================


def initialize_board():
    """
    Initializes an empty board.
    :return: a BOARD_SIZE * BOARD_SIZE list of lists (matrix). Each cell initialized with WATER.
    """
    board = [[0] * BOARD_SIZE for i in range(BOARD_SIZE)]

    for row in range(BOARD_SIZE):
        for cell in range(BOARD_SIZE):
            board[row][cell] = WATER

    return board


def print_board(board, show_ships=False):
    """
    Prints the game board to the command line.
    :param board: game board to print
    :param show_ships: whether to show where the ships are placed or not.
    """
    print('___________')
    for row in board:
        for value in row:
            value = WATER if not show_ships and value == SHIP else value
            print('|' + value, end="")

        print('|\n-----------')
    print('')


def place_enemy_ships(board):
    """
    Places enemy boats on the board at random.
    :param board: game board

    Already provided.
    """
    # Used to make sure we do not loop forever!
    iteration_count = 0

    boats_positioned = 0
    while boats_positioned < NUMBER_OF_SHIPS and iteration_count < 100:
        iteration_count += 1
        new_coordinates = random_coordinates(len(board))
        if place_ship(board, new_coordinates):
            boats_positioned += 1


def place_ship(board, coordinates):
    """
    Place a boat at position.
        - If coordinates are valid for a ship placement, set board cell to SHIP, return True
        - Else False
    :param board: game board
    :param coordinates: coordinates where we want to place a ship
    :return: True if placement was valid (coordinates valid and not yet taken), false otherwise.
    """
    if are_coordinates_valid(board, coordinates):
        if board[coordinates[0]][coordinates[1]] == WATER:
            board[coordinates[0]][coordinates[1]] = SHIP
            return True
        else:
            return False
    else:
        return False


def fire(board, coordinates):
    """
    Fires at coordinates:
        - If at coordinates there is a ship floating, then set the board cell to SUNK_SHIP, return True
        - If at coordinates there is no ship, then set the board cell to MISSED_SHOT, return False
        - If at coordinates there is an already sunk ship, then leave the board cell as SUNK_SHIP, return False
        - If coordinates are not valid, then leave board unchanged, return False

    Returns true if its a hit, false otherwise or if invalid coordinates.
    :param board: game board
    :param coordinates: coordinates to fire at
    :return: True iff coordinates mark a floating ship, False if water, ship already sunk or coordinates are invalid.
    """

    if are_coordinates_valid(board, coordinates):
        if board[coordinates[0]][coordinates[1]] == SHIP:
            board[coordinates[0]][coordinates[1]] = SUNK_SHIP
            return True

        elif board[coordinates[0]][coordinates[1]] == WATER:
            board[coordinates[0]][coordinates[1]] = MISSED_SHOT
            return False

        elif board[coordinates[0]][coordinates[1]] == SUNK_SHIP:
            return False

    else:
        return False


def are_coordinates_valid(board, coordinates):
    """
    Checks if coordinates are valid, i.e. inside the board.
    :param board: needed to check size of board
    :param coordinates: coordinates to check for validity
    :return: True iff valid else False
    """
    board_size = len(board)

    if coordinates[0] > board_size - 1 or coordinates[1] > board_size - 1:
        return False
    elif coordinates[0] < 0 or coordinates[1] < 0:
        return False
    else:
        return True


def are_valid_ship_coordinates(board, coordinates):
    """
    Checks if coordinates are valid for ship placement: valid coordinates and no ship is already at coordinates.
    :param board: game board
    :param coordinates: coordinates to check for valid ship placement
    :return: True iff a ship can be placed at coordinates else False
    """

    if are_coordinates_valid(board, coordinates):
        if board[coordinates[0]][coordinates[1]] == SHIP:
            return False
        else:
            return True
    else:
        return False


def is_game_over(board):
    """
    Are there no more ships floating?
    :param board: game board.
    :return: True there is no ship floating left else False
    """
    for row in range(len(board)):
        for cell in range(len(board)):
            if board[row][cell] == SHIP:
                return False
            else:
                continue

    return True


def get_coordinates_from_user():
    """
    Asks the users for 'x' and 'y' coordinates and returns a tuple (x, y).

    :return: A tuple of coordinates. There is no need to check if the coordinates are valid at this point.
    Checks should be done inside the fire function.

    Note: a user can enter coordinates like this in the command line:
    "Coordinates? 0,1"
    """
    return tuple(map(int, input('Coordinates? ').split(',')))


def random_coordinates(size):
    return randint(0, size - 1), randint(0, size - 1)


def compute_statistics(board):
    """
    Computes game statistics:
    - turns_taken: count('-') + count('X')
    - hit_ratio: count('X') / turns_taken
    - ships_floating: count('O')

    :return: a tuple of tuples: (('Turns taken', turns_taken), ('Hit ratio', hit_ratio), ('Ship still floating', ships_floating))
    """
    count_missed = sum(row.count('-') for row in board)
    count_hits = sum(row.count('X') for row in board)
    ships_floating = sum(row.count('O') for row in board)
    turns_taken = count_missed + count_hits
    hit_ratio = count_hits / turns_taken if turns_taken != 0 else 0

    return ('Turns taken', turns_taken), ('Hit ratio', hit_ratio), ('Ships still floating', ships_floating)


def play():
    """
    Game logic.

    Initialize an empty board.
    Place enemy ships.
    Print initial board.

    While not game over
        1. Get user input
        2. fire
        3. print board, statistics
    """

    print("Good luck!")
    game_board = initialize_board()
    place_enemy_ships(game_board)
    print_board(game_board)

    while not is_game_over(game_board):
        coordinates = get_coordinates_from_user()
        has_hit = fire(game_board, coordinates)

        print_board(game_board)
        print("{}".format('Direct hit!' if has_hit else 'Missed...'))

        for stat in compute_statistics(game_board):
            print(stat[0], stat[1])

    print("Game over!")


if __name__ == '__main__':

    board = initialize_board()

    print(are_coordinates_valid(board, (11, 0)))
