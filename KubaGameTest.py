# Author: Fahad Awan
# Date: 6/6/2021
# Description:

import unittest
from KubaGame import KubaGame

class TestGame(unittest.TestCase):
    # ['W', 'W', "X", "X", "X", 'B', 'B']
    # ['W', 'W', "X", 'R', "X", 'B', 'B']
    # ["X", "X", 'R', 'R', 'R', "X", "X"]
    # ["X", 'R', 'R', 'R', 'R', 'R', "X"]
    # ["X", "X", 'R', 'R', 'R', "X", "X"]
    # ['B', 'B', "X", 'R', "X", 'W', 'W']
    # ['B', 'B', "X", "X", "X", 'W', 'W']

    def setUp(self) -> None:
        # create instance
        self.game=KubaGame(("player1", "B"), ("player2", "W"))



    def test_move_L(self):
        # basic move from start of game
        self.game.move((5,1), "L")
        self.assertEqual(self.game.get_board()[5], ['B', "X", "X", 'R', "X", 'W', 'W'])


    def test_move_R(self):
        # basic move from start of game
        self.game.move((5, 5), "R")
        self.assertEqual(self.game.get_board()[5], ['B', 'B', "X", 'R', "X", "X", 'W'])


    def test_move_B(self):
        # basic move from start of game
        self.game.move((5, 5), "B")
        self.assertEqual(self.game.get_column(5), ['B', 'B', "X", 'R', "X", "X", 'W'])

    def test_move_F(self):
        # basic move from start of game
        self.game.move((0, 6), "F")
        self.assertEqual(self.game.get_column(6), ['B', "X", "X", "X", "X", 'W', 'W'])

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
    # ['W', 'W', "X", "X", "X", 'B', 'B']
    # ['W', 'W', "X", 'R', "X", 'B', 'B']
    # ["X", "X", 'R', 'R', 'R', "X", "X"]
    # ["X", 'R', 'R', 'R', 'R', 'R', "X"]
    # ["X", "X", 'R', 'R', 'R', "X", "X"]
    # ['B', 'B', "X", 'R', "X", 'W', 'W']
    # ['B', 'B', "X", "X", "X", 'W', 'W']
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
        self.game.add_marble_count("X", name)
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

    def test_push_off_red(self):
        name="player1" #black
        opposing='player2'

        self.game.set_board(
       [
            ['W', 'W', "X",  'W',  "X",  'B',  'B'],
            ['W', 'W', "X",  'B',  "X",  'B',  'B'],
            ["X",  "X",  "X",  'W',  "X",   "X",  "X"],
            ["X",  'W', 'R', 'R', 'R',  'R',  "X"],
            ["X",  'R', 'R', 'R', 'R',  "X",   "X"],
            ["X",  'B', "X",  'R',  "X",  'W', 'W'],
            ["X",  'R', "X",  'B',  "X",  'W', 'W']
       ])
        marbles=self.game.get_marble_count()
        white, black, red=marbles[0], marbles[1], marbles[2]

        # turn inited to None
        self.assertEqual(self.game.get_current_turn(), None)
        # player1 starts game
        self.assertTrue(self.game.make_move(name, (6,3), "F"))
        # move was valid, should be player2's turn
        self.assertEqual(self.game.get_current_turn(), opposing)
        # pushed off white, no red captured
        self.assertEqual(self.game.get_captured(name), 0)
        # check black marble count
        self.assertEqual(self.game.get_remaining(name), 8)
        # white marble count reduced by 1
        self.assertEqual(self.game.get_remaining(opposing), 7)
        # check marble count. white has been reduced by 1
        self.assertEqual(self.game.get_marble_count(), (white-1,black,red))
        # player2 push off red marble
        self.assertTrue(self.game.make_move(opposing, (3,1), "B"))
        # move was valid, should be player1's turn
        self.assertEqual(self.game.get_current_turn(), name)
        # player 2 captured a red
        self.assertEqual(self.game.get_captured(opposing),1)
        # check marble counter. white was reduced by 1 previously, red now reduced by 1
        self.assertEqual(self.game.get_marble_count(), (white-1, black, red-1))
        # player1 try push off own marble, this shouldn't work
        self.assertFalse(self.game.make_move(name, (1,6), "F"))
        # check marble count
        self.assertEqual(self.game.get_marble_count(), (white-1, black, red-1))
        # should still be player1's turn
        self.assertEqual(self.game.get_current_turn(), name)

    def test_winning_eliminated_opposing_marbles(self):
        name="player2" # white
        opposing="player1" # black
        self.game.set_board( [
            ['W', 'W', "X",  'W',  "X",  "X",  "X"],
            ['W', 'W', "X",  'R',  "X",  "X",  "X"],
            ["X",  "X",  "X",  'W',  "X",   "X",  "X"],
            ["X",  'W', 'R', 'R', 'R',  'R',  "X"],
            ["X",  'R', 'R', 'R', 'R',  "X",   "X"],
            ["X",  'W', "X",  'R',  "X",  'W', 'W'],
            ["X",  'R', "X",  'B',  "X",  'W', 'W']
       ])
        # set black marble count to 1 for testing
        self.game._players[opposing]["remaining"]=1
        # push off last black marble
        self.assertTrue(self.game.make_move(name, (0,3), "B"))
        # check count of black marbles
        self.assertEqual(self.game.get_remaining(opposing),0)
        # check winner, white should have won
        self.assertEqual(self.game.get_winner(),"player2")
        # try and make move after a winner is found
        self.assertFalse(self.game.make_move(opposing,(2,2), "B"))

    def test_winning_7red_marbles(self):
        name = "player2"  # white
        opposing = "player1"  # black
        self.game.set_board([
            ['W', 'W', "X", "X", "X", "X", "X"],
            ['W', 'W', "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", 'W', "X", 'R', "X", 'W', 'W'],
            ["X", 'R', "X", 'B', "X", 'W', 'W']
        ])
        # set red marbles captured for player2 to 6
        self.game._captured[name]=6
        self.assertEqual(self.game.get_captured(name), 6)
        # capture 7th red marble
        self.assertTrue(self.game.make_move(name, (5,1), "B"))
        # check winner
        self.assertEqual(self.game.get_winner(),name)
        # try and make move after a winner is found
        self.assertFalse(self.game.make_move(opposing, (6, 3), "F"))



