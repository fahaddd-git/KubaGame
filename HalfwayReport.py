# Author: Fahad Awan
# Date: 5/25/2021
# Description: High level overview plan of the KubaGame class for Halfway Report assignment.

class KubaGame:
    """Singular class to play the KubaGame. Encompasses entire project. Includes board, two players, 3 kinds of marbles,
     and the rules of how to play.
    """

    def __init__(self, player1, player2):
        """Initializer for the Kuba Game. Assigns player marble colors and creates board. Also initializes variables for
        current player's turn, winner if any, and marbles remaining/captured for each player.
        :param player1 tuple: contains player name and color of the marble that the player is playing B or W
        :param player1 tuple: contains player name and color of the marble that the player is playing B or W
        """
        # # players of the game  {player1name: {color: , red_marbles:}}
        # self._players = {player1[0]: {"name": player1[0], "color": player1[1]},
        #                  player2[0]: {"name": player2[0], "color": player2[1]}}
        # # empty board, no marbles yet
        # self._board = self.create_board()
        # # current player's turn
        # self._turn = None
        # # winner state
        # self._winner = None
        # # red marbles captured for each player, needs addition of black and white marbles
        # self._captured = {player1[0]: 0, player2[0]: 0}
        pass

    def create_board(self):
        """Creates and returns starting iteration of the game board."""
        # # empty 7x7 board
        # board = [[list() for x in range(7)] for y in range(7)]
        # # coordinates of starting marbles
        # black = [[0, 0], [1, 0], [1, 1], [0, 1], [6, 6], [6, 5], [5, 5], [5, 6]]
        # white = [[6, 0], [6, 1], [5, 1], [5, 0], [0, 6], [0, 5], [1, 5], [1, 6]]
        # red = [[1, 3], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4], [5, 3]]
        # for marble in white:
        #     board[marble[0]][marble[1]] = "B"
        # for marble in black:
        #     board[marble[0]][marble[1]] = "W"
        # for marble in red:
        #     board[marble[0]][marble[1]] = "R"
        # return board
        pass

    def print_board(self):
        """Prints a visual representation of the current board."""
        print(*self._board, sep="\n")

    def get_board(self):
        """Returns current board."""
        return self._board

    def get_winner(self):
        """Returns current game winner or None if no winner yet."""
        return self._winner

    def get_opposing_player(self, player_name):
        """Given a player, returns the opposing player's name.
        :param player_name String: a player's name"""
        pass

    def update_turn(self):
        """Sets turn be the opposing player."""
        pass

    def previous_board(self):
        """Creates a deep copy of the board and assigns it to self._previous_board."""
        pass

    def get_current_turn(self):
        """Returns which player's turn it is to play."""
        return self._turn

    def is_players_marble(self, player_name, coordinates):
        """Checks for a given player's marble and returns true if the marble at the coordinate is the given
        player's marble. Else returns false if no marble at location, red marble, or opposing player's marble.
        :param player_name string: name of the player
        :param coordinates tuple: location on the game board where to check"""
        pass

    def get_marble(self, coordinates):
        """Returns which color marble is present at the given coordinates.
        If no marble present returns X.
        :param coordinates tuple: coordinates of where to locate the requested marble"""
        pass

    def get_captured(self, player_name):
        """Returns amount of red marbles captured for a given player name. If no player exists returns "no player exists"
        :param player_name String: name of player to look up red marble count
        """
        pass
    def get_marble_count(self):
        """Returns tuple of current amount of W, B, R marbles remaining on the board."""

    def ko_rule(self):
        """Returns true or false whether the proposed move is in violation of the ko rule"""
        pass

    def move_marble(self, coordinates, direction):
        """Checks to see if the move is valid in the given direction at the given coordinates. Checks current game board
        to see if the marble is surrounded from the direction of movement or if the move pushes off same color marble.
        Returns True or False.
        :param coordinates tuple: coordinates of the marble to be moved
        :param direction String: direction to move the marble (L, R, F, or B)"""
        pass


    def move(self, coordinates, direction):
        """Moves a marble at the coordinates in the given direction. Updates marble count for
        each player if marble is captured or pushed off. Updates previous_board then updates game board.
        :param playername String: name of the player making the move
        :param coordinates tuple: coordinates of the marble to be moved
        :param direction String: direction to move the marble at the specified coordinates. Valid directions are L, R, F, B"""
        pass

    def check_winner(self):
        """Returns True or False whether a winner has been reached. Sums the red marbles of each player and checks if
        players have any marbles remaining"""
        pass

    def make_move(self, playername, coordinates, direction):
        """Makes a move on the game board. If the move is successful returns True else returns False.
        :param playername String: name of the player making the move
        :param coordinates tuple: coordinates of the marble to be moved
        :param direction String: direction to move the marble at the specified coordinates. Valid directions are L, R, F, B"""

        pass






#                   DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
#
# -----------------------------------Initializing the board-------------------------------------------------------------
#
#   - the entire game, players, marbles and rules will be encapsulated in the KubaGame class.
#       -initializer method
#           - receives and unpack tuples from user into a class variable player dictionary object
#           - create a representation of the board using create_board (see below)
#           - create class variables for current turn and winner
#           - create class variables to keep track of marbles captured per player and marbles remaining
#           - create class variable to hold previous state of the board
#
#
# Initializing the game board representation will be done by calling the create_board method in the initializer for
#   the KubaGame class.
#
# create_board:
#   - use nested list iterators to create a 7x7 grid to represent the game board
#   - contain data to represent where on the board to place the starting white, red, and black marbles.  This data will
#          be represented as a list of coordinates.
#   - iterate over each of the list of coordinates. For each kind of marble data, place the corresponding letter at that
#          coordinate. ("R" for red, "B" for black, "W" for white)
#
# ------------------- Determining how to track which player's turn it is to play right now.-----------------------------
#
#   - initialize the KubaGame class current player's turn variable (self._turn) to None since either player can start
#       the game
#   - use a number of methods to update current player's turn and view the opposition:
#         - get_current_turn
#               - returns the current player of the game (class variable self._turn)
#         - get_opposing_player
#               - receives the current player from get_turn
#               - iterates through player's dictionary and creates list of player names
#               - compares names of players and returns the opposing player
#               - if game has not started returns None
#         - update_turn
#               - uses get_opposing_player to get the opposing player's name
#               - sets current player (self._turn) to be the received get_opposing_player
#
# --------------------------------- Determining how to validate a move.-------------------------------------------------
#
#   First, check if the move is invalid. The conditions of an invalid move are if the move is being made after the game
#   has been won, it's not the player's turn, if the coordinates provided are not valid, a marble in the coordinates
#   cannot be moved in the direction specified, it is not the current player's marble, it is a red marble,
#   the ko rule is invoked, the move pushes off own marble.
#
#   -  make_move method calls other helper methods and variables for validation.
#       These are invalid move conditions which can be handled by a sentinel in the beginning of the function:
#       - check class variable self._winner is not None to see if the game has been won using get_winner
#       - call get_opposing_player to see if it is the opposing player's turn (this accounts for starting the game too)
#       - call get_marble to see if there is marble at the given coordinates.
#           - if get_marble returns "X", a red marble, or the opposing player's marble then move invalid
#       - call ko_rule
#           - if previous validation checks pass, attempt the given move
#           - iterate through each row of the deep copy of the game board self._previous_board
#           - compare each row with the proposed move on the game board to see if the spaces and symbols match
#           - if they are the same, ko_rule returns True and the move is invalid.
#       - call move_marble
#           - iterates through row or column (depending on move direction)
#           - check if another marble is at index next to given coordinates in the given direction (return False)
#           - check if marble at end of board in direction of push is same color (return False)
#           - otherwise call move function and return True
#
# ---------------------------- Determine how to return the marble count.------------------------------------------------
#
#   - Store marble counter for each player is stored in class variables self._captured dictionary
#       - created during class initialization
#       - holds player names and counts of R and B/W marbles
#   - get_marble_count
#       - iterate through self._captured dictionary and sum captured marbles of each color
#       - subtract each type from amount of W, B, R marbles game allows
#       - return tuple of (W,B,R) marbles remaining on board
#   - check_winner
#       - check_winner is called after executing a move using move function
#       - checks the amount of red marbles of each player in self._captured using get_captured
#       - if a player has 7 R, set player to be the winner
#       - if a player has no B or W, set other player in dictionary to be the winner
#
# --------------------------Determine how to move the marbles on the board.---------------------------------------------

#   - only possible if move_marble returns True
#   - determine from user input which direction marble will be moving. Call move function.
#       - move
#           - if moving B or F, iterate through column of game board
#           - if moving L or R, iterate through row of game board
#           - iterate through indices in the given direction until an empty slot is reached on board or
#               end of board reached
#           - create slice of board up to empty or out of range index
#           - reassign slice to the incremented (or decremented) new index position
#           - if no empty slot/IndexError, a marble has been pushed off
#               - increment/decrement player's marble counts
#               - call check_winner to see if a winner has been reached
#               - return True
#
#