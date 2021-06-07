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
        self.assertEqual(self.game.get_column(6), ['B', [], [], [], [], 'W', 'W'])

    def test_marble_count_initial(self):
        # initial marble count tuple (W, B, R)
        initial_count=self.game.get_marble_count()
        self.assertEqual(initial_count,(8,8,13))

    def test_initial_winner(self):
        # winner should be init to None
        winner=self.game.get_winner()
        self.assertEqual(winner, None)

    def test_get_captured(self):
        # red marbles captured initially
        self.assertEqual(self.game.get_captured("player2"), 0)
    # ['W', 'W', [], [], [], 'B', 'B']
    # ['W', 'W', [], 'R', [], 'B', 'B']
    # [[], [], 'R', 'R', 'R', [], []]
    # [[], 'R', 'R', 'R', 'R', 'R', []]
    # [[], [], 'R', 'R', 'R', [], []]
    # ['B', 'B', [], 'R', [], 'W', 'W']
    # ['B', 'B', [], [], [], 'W', 'W']
    def test_validate_move_false(self):
        name="player2"
        #attempt to push off own marble moving F and B
        self.assertFalse(self.game.validate_move(name,(0,1), "F"))
        self.assertFalse(self.game.validate_move(name,(5,6), "B"))
        # attempt to move F and B but a marble blocking
        self.assertFalse(self.game.validate_move(name,(1,1), "B"))
        self.assertFalse(self.game.validate_move(name,(5,6), "F"))
        # attempt to push off own marble moving L and R
        self.assertFalse(self.game.validate_move(name,(0,1), "L"))
        self.assertFalse(self.game.validate_move(name,(6,5), "R"))
        # attempt to move L and R but a marble blocking
        self.assertFalse(self.game.validate_move(name,(0,0), "L"))
        self.assertFalse(self.game.validate_move(name,(6,6), "R"))

        # invalid coordinates
        self.assertFalse(self.game.validate_move(name, (0,-2), "F"))
        # not this player's marble
        self.assertFalse(self.game.validate_move(name, (6,0), "L"))
        # try to push red marble
        self.assertFalse(self.game.validate_move(name, (2,1), "R"))
        # game already won
        self.game._winner=name
        self.assertFalse(self.game.validate_move(name, (0,0), "R"))



    def test_validate_move_true(self):
        name="player1"
        # push own marbles L and R
        self.assertTrue(self.game.validate_move(name, (0,6), "L"))
        self.assertTrue(self.game.validate_move(name, (6,0), "R"))

    def test_get_marble(self):
        # test with negative indices
        self.assertEqual(self.game.get_marble((1,-1)), "X")

    def test_get_opposing_player(self):
        # test get_opposing_player func
        self.assertEqual(self.game.get_opposing_player("player2"), "player1")

    def test_add_marble_count(self):
        # adding to marble counters
        name="player1" # Black
        opposition="player2"
        # no marble captured
        self.game.add_marble_count([], name)
        self.assertEqual(self.game.get_captured(name), 0)
        # opposing color marble captured
        self.game.add_marble_count("W", name)
        self.assertEqual(self.game.get_captured(name), 0) # not a red marble
        self.assertEqual(self.game.get_remaining(opposition), 7) # count of opposing player's marbles
        # red marble captured
        self.game.add_marble_count("R", name)
        self.assertEqual(self.game.get_captured(name), 1)
        # own marble captured (shouldn't be possible)
        self.game.add_marble_count("B", name)
        self.assertEqual(self.game.get_remaining(name), 8)  # count of opposing player's marbles
