# Author: Fahad Awan
# Date: 6/6/2021
# Description:

import unittest
from KubaGame import KubaGame

class TestGame(unittest.TestCase):
    # ['W', 'W', [], [], [], 'B', 'B']
    # ['W', 'W', [], 'R', [], 'B', 'B']
    # [[], [], 'R', 'R', 'R', [], []]
    # [[], 'R', 'R', 'R', 'R', 'R', []]
    # [[], [], 'R', 'R', 'R', [], []]
    # ['B', 'B', [], 'R', [], 'W', 'W']
    # ['B', 'B', [], [], [], 'W', 'W']

    def setUp(self) -> None:
        # create instance
        self.game=KubaGame(("player1", "B"), ("player2", "W"))


    def test_move_L(self):
        # basic move from start of game
        self.game.move((5,1), "L")
        self.assertEqual(self.game.get_board()[5], ['B', [], [], 'R', [], 'W', 'W'])


    def test_move_R(self):
        # basic move from start of game
        self.game.move((5, 5), "R")
        self.assertEqual(self.game.get_board()[5], ['B', 'B', [], 'R', [], [], 'W'])


    def test_move_B(self):
        # basic move from start of game
        self.game.move((5, 5), "B")
        self.assertEqual(self.game.get_column(5), ['B', 'B', [], 'R', [], [], 'W'])



    def test_move_F(self):
        # basic move from start of game
        self.game.move((0, 6), "F")
        self.assertEqual(self.game.get_column(6), ['B', [], [], 'R', [], 'W', 'W'])

