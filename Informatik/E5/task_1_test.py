import unittest
from unittest import TestCase
from unittest.mock import patch

import task_1 as student_submission


class Task1Test(TestCase):
    """
    Task 1: Battleship
    """

    def test_has_initialize_board(self):
        """Has initialize board"""
        self.assertTrue(hasattr(student_submission, "initialize_board"), "You must declare 'initialize_board'")

    def test_initialize_board(self):
        """Initialize board creates an empty board"""
        board = student_submission.initialize_board()

        is_empty = filter(lambda row: row.all(lambda value: value == student_submission.WATER), board)
        self.assertTrue(is_empty, 'The board does not seem to have been initialized correctly')

        test_value = 'TEST'
        board[1][1] = test_value

        count_test_values = sum(row.count(test_value) for row in board)
        self.assertEqual(count_test_values, 1, 'Modifying any nested list, modifies all other lists as well!')

    def test_place_enemy_ships(self):
        """Placing enemy ships works and places the correct number of ships"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        student_submission.place_enemy_ships(board)

        count_boats = sum(row.count(student_submission.SHIP) for row in board)
        self.assertEqual(count_boats, student_submission.NUMBER_OF_SHIPS,
                         '"place_enemy_boats" is not spawning {} ships'.format(student_submission.NUMBER_OF_SHIPS))

    def test_place_ship(self):
        """Placing a single ship in a free spot works"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        coordinates = (0, 0)
        placed = student_submission.place_ship(board, coordinates)
        self.assertTrue(placed, 'Failed to place a ship')

        count_boats = sum(row.count(student_submission.SHIP) for row in board)
        self.assertEqual(board[coordinates[0]][coordinates[1]], student_submission.SHIP,
                         '"place_ship" did not place a ship at coordinates {}'.format(coordinates))
        self.assertEqual(count_boats, 1,
                         '"place_enemy_boats" is not spawning {} ships'.format(student_submission.NUMBER_OF_SHIPS))

    def test_place_ship_at_invalid_coordinates(self):
        """Placing a single ship at invalid coordinates does not work"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        invalid_coordinates = (-1, 0)
        placed = student_submission.place_ship(board, invalid_coordinates)
        self.assertFalse(placed, 'Failed to place a ship')

        count_boats = sum(row.count(student_submission.SHIP) for row in board)
        self.assertEqual(count_boats, 0,
                         '"place_ship" spawned a ship at invalid coordinates {}'.format(invalid_coordinates))

        invalid_coordinates = (0, -1)
        placed = student_submission.place_ship(board, invalid_coordinates)
        self.assertFalse(placed, 'Failed to place a ship')

        count_boats = sum(row.count(student_submission.SHIP) for row in board)
        self.assertEqual(count_boats, 0,
                         '"place_ship" spawned a ship at invalid coordinates {}'.format(invalid_coordinates))

    def test_place_ship_at_coordinates_with_ship(self):
        """Placing a single ship where another ship is should not work"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        board[0][0] = student_submission.SHIP

        coordinates = (0, 0)
        placed = student_submission.place_ship(board, coordinates)
        self.assertFalse(placed, 'Failed to place a ship')

    def test_fire_at_water(self):
        """Firing at empty spot should set a marker and return False"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        board[0][0] = student_submission.WATER

        sunk_ship = student_submission.fire(board, (0, 0))
        self.assertFalse(sunk_ship, 'Sunk ship while shooting at water!')
        self.assertEqual(board[0][0], student_submission.MISSED_SHOT,
                         'Missing the shot should place a missed shot symbol at coordinates {}'.format((0, 0)))

    def test_fire_at_ship(self):
        """Firing at ship should sink it and return True"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        board[0][0] = student_submission.SHIP
        board[student_submission.BOARD_SIZE - 1][student_submission.BOARD_SIZE - 1] = student_submission.SHIP

        sunk_ship = student_submission.fire(board, (0, 0))
        self.assertTrue(sunk_ship, 'Shooting at ship did not work!')
        self.assertEqual(board[0][0], student_submission.SUNK_SHIP,
                         'Shooting at the ship at {} did not work!'.format((0, 0)))

    def test_fire_at_invalid_coordinates(self):
        """Firing at invalid coordinates should not do anything and return False"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]

        invalid_coordinates = (-1, 0)
        sunk_ship = student_submission.fire(board, invalid_coordinates)
        self.assertFalse(sunk_ship, 'Shooting at invalid coordinates {} worked!'.format(invalid_coordinates))

        invalid_coordinates = (student_submission.BOARD_SIZE, 0)
        sunk_ship = student_submission.fire(board, invalid_coordinates)
        self.assertFalse(sunk_ship, 'Shooting at invalid coordinates {} worked!'.format(invalid_coordinates))

    def test_are_coordinates_valid(self):
        """Are valid coordinates valid"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        self.assertTrue(student_submission.are_coordinates_valid(board, (0, 0)))
        self.assertTrue(student_submission.are_coordinates_valid(board, (len(board) - 1, 0)))

    def test_are_coordinates_valid_invalid(self):
        """Are invalid coordinates valid"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        self.assertFalse(student_submission.are_coordinates_valid(board, (-1, 0)))
        self.assertFalse(student_submission.are_coordinates_valid(board, (len(board), 0)))

    def test_board_with_all_ships_sunken_is_not_game_over(self):
        """A board with no ships still floating should result in game over"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]
        board[0][0] = student_submission.SUNK_SHIP
        self.assertTrue(student_submission.is_game_over(board),
                        'The board still has no ships floating! It should be game over')

    def test_statistics(self):
        """Compute statistics"""
        board = [[student_submission.WATER for i in range(5)] for i in range(5)]

        board[0][0] = student_submission.SHIP
        board[0][1] = student_submission.SHIP
        board[2][0] = student_submission.SHIP
        board[3][3] = student_submission.SHIP
        board[3][4] = student_submission.SHIP
        statistics = student_submission.compute_statistics(board)

        self.assertEqual(statistics[0][1], 0)
        self.assertEqual(statistics[1][1], 0)
        self.assertEqual(statistics[2][1], 5)

        board[3][4] = student_submission.SUNK_SHIP

        statistics = student_submission.compute_statistics(board)

        self.assertEqual(statistics[0][1], 1)
        self.assertAlmostEqual(statistics[1][1], 1, delta=0.1)
        self.assertEqual(statistics[2][1], 4)

        board[1][1] = student_submission.MISSED_SHOT

        statistics = student_submission.compute_statistics(board)

        self.assertEqual(statistics[0][1], 2)
        self.assertAlmostEqual(statistics[1][1], 0.5, delta=0.1)
        self.assertEqual(statistics[2][1], 4)

        board[0][1] = student_submission.SUNK_SHIP

        statistics = student_submission.compute_statistics(board)

        self.assertEqual(statistics[0][1], 3)
        self.assertAlmostEqual(statistics[1][1], 2 / 3, delta=0.1)
        self.assertEqual(statistics[2][1], 3)

    def test_game_is_playable(self):
        """Game is playable from start to finish. Warning: might end up in an infinite loop!"""
        size = student_submission.BOARD_SIZE
        moves = ['{},{}'.format(i, j) for i in range(size) for j in range(size)]

        with patch('builtins.input', side_effect=moves):
            student_submission.play()


if __name__ == '__main__':
    unittest.main(verbosity=2)
