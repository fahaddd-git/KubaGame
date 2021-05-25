# Author: Fahad Awan
# Date: 5/25/2021
# Description:

class KubaGame:
    def __init__(self, player1, player2):
        """Initializer for the Kuba Game. Assigns player marble colors and creates board.
        :param player1 tuple: contains player name and color of the marble that the player is playing R, B, or W
        :param player1 tuple: contains player name and color of the marble that the player is playing R, B, or W
        """
        # players of the game  {player1name: {color: , red_marbles:
        self._player1={"name": player1[0],"color": player1[1]}
        self._player2={"name": player2[0], "color":player2[1]}
        # empty board, no marbles yet
        self._board= self.create_board()
        # current player's turn
        self._turn=None
        # winner state
        self._winner=None

    def create_board(self):
        """Creates starting iteration of the game board"""
        # empty 7x7 board
        board=[[list() for x in range(7)] for y in range (7)]
        # coordinates of starting marbles
        black= [[0,0], [1,0], [1,1], [0,1],[6,6], [6,5], [5,5], [5,6]]
        white=[[6,0], [6,1], [5,1], [5,0], [0,6], [0,5],[1,5], [1,6]]
        red=[[1,3],[2,2], [2,3], [2,4], [3,1], [3,2], [3,3], [3,4], [3,5], [4,2], [4,3], [4, 4], [5,3]]
        for marble in white:
            board[marble[0]][marble[1]]="B"
        for marble in black:
            board[marble[0]][marble[1]]="W"
        for marble in red:
            board[marble[0]][marble[1]]="R"
        return board

    def print_board(self):
        """Prints the current board."""
        print(*self._board, sep="\n")

    def get_board(self):
        """Returns current board."""
        return self._board

    def get_winner(self):
        """Returns current game winner."""
        return self._winner


    def update_turn(self):
        """Sets turn be the opposing player."""

        if self._turn==self._player1:
            self._turn=self._player2
        elif self._turn==self._player2:
            self._turn=self._player1


    def get_turn(self):
        """Returns which player's turn it is to play."""
        return self._turn

    def get_marble(self, coordinates):
        """Returns which color marble is present at the given coordinates.
        If no marble present returns X.
        :param coordinates tuple: coordinates of where to locate the requested marble"""
        try:
            # no marble at given coordinates
            if self._board[coordinates[0]][coordinates[1]]==[]:
                return "X"
            else:
                return self._board[coordinates[0]][coordinates[1]]
        # coordinate was out of range
        except IndexError:
            return "X"




testgame=KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
testgame.print_board()
print(testgame.get_marble((6,0)))