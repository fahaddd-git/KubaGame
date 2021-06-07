# Author: Fahad Awan
# Date: 5/25/2021
# Description:

class KubaGame:
    def __init__(self, player1, player2):
        """Initializer for the Kuba Game. Assigns player marble colors and creates board.
        :param player1 tuple: contains player name and color of the marble that the player is playing B or W
        :param player1 tuple: contains player name and color of the marble that the player is playing B or W
        """
        # players of the game  {player1name: {color: , red_marbles:
        self._players = {player1[0]: {"name": player1[0], "color": player1[1]},
                         player2[0]: {"name": player2[0], "color": player2[1]}}
        # empty board, no marbles yet
        self._board = self.create_board()
        # current player's turn
        self._turn = None
        # winner state
        self._winner = None
        # red marbles captured for each player
        self._captured = {player1[0]: 0, player2[0]: 0}

    def create_board(self):
        """Creates starting iteration of the game board"""
        # empty 7x7 board
        board = [[list() for x in range(7)] for y in range(7)]
        # coordinates of starting marbles
        black = [[0, 0], [1, 0], [1, 1], [0, 1], [6, 6], [6, 5], [5, 5], [5, 6]]
        white = [[6, 0], [6, 1], [5, 1], [5, 0], [0, 6], [0, 5], [1, 5], [1, 6]]
        red = [[1, 3], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 2], [4, 3], [4, 4], [5, 3]]
        for marble in white:
            board[marble[0]][marble[1]] = "B"
        for marble in black:
            board[marble[0]][marble[1]] = "W"
        for marble in red:
            board[marble[0]][marble[1]] = "R"
        return board

    def print_board(self):
        """Prints the current board."""
        print(*self._board, sep="\n")

    def get_board(self):
        """Returns current board."""
        return self._board

    def get_winner(self):
        """Returns current game winner or None if no winner yet."""
        return self._winner

    def get_opposing_player(self, player_name):
        """Returns the opposing player's name.
        :param player_name String: a player's name"""
        players_keys = list(self._players.keys())
        if player_name == players_keys[0]:
            return players_keys[1]
        else:
            return players_keys[0]

    def update_turn(self):
        """Sets turn be the opposing player."""
        # was player 1's turn, change to player 2's turn
        players_keys = list(self._players.keys())

        if self._turn == players_keys[0]:
            self._turn = players_keys[1]
        # was player 2's turn, change to player 1's turn
        elif self._turn == players_keys[1]:
            self._turn = players_keys[0]

    def get_current_turn(self):
        """Returns which player's turn it is to play."""
        return self._turn

    def is_players_marble(self, player_name, coordinates):
        """Returns true if the marble at the coordinate is the given player's marble.
        :param player_name string: name of the player
        :param coordinates tuple: location on the game board where to check"""
        # requested space is not the color of the player_name's marble or empty
        if self._players[player_name]["color"] != self.get_marble(coordinates):
            return False
        # requested space is the color of the player_name's marble
        if self._players[player_name]["color"] == self.get_marble(coordinates):
            return True

    def get_marble(self, coordinates):
        """Returns which color marble is present at the given coordinates.
        If no marble present returns X.
        :param coordinates tuple: coordinates of where to locate the requested marble"""

        row,col=coordinates[0],coordinates[1]

        try:
            # no marble at given coordinates
            if self._board[coordinates[0]][coordinates[1]] == []:
                return "X"
            if row <0 or col<0:
                return "X"

        # coord out of range
        except IndexError:
                return "X"
        # passed tests, must exist
        return self._board[coordinates[0]][coordinates[1]]



    def get_column(self, column):
        """
        :param coordinates tuple:
        :return: column at coordinate location as a list
        """
        return [tile[column] for tile in self._board]



    def move(self, coords, direction):
        """
        :param coords: tuple
        :param row: list
        :return:
        """
        row_length = len(self._board) - 1

        # left movement
        if direction == 'L':
            row = self._board[coords[0]]
            # column coordinate is length of row-given coord
            coord_row, coord_col = coords[0], row_length - coords[1]
            # reverse row
            row.reverse()

        # right movement
        elif direction == 'R':
            row = self._board[coords[0]]
            # unpack coords
            coord_row, coord_col = coords[0], coords[1]

        # backwards movement
        elif direction == "B":
            # flipped row/ col for vertical mvt
            coord_row, coord_col = coords[1], coords[0]
            row = [tile[coord_row] for tile in self._board]

        # forwards movement
        elif direction == "F":
            coord_row, coord_col = coords[1], row_length - coords[0]
            row = [tile[coord_row] for tile in self._board]
            row.reverse()

        # gives index of next empty spaces (if any)
        for index, item in enumerate(row, start=0):
            # if the empty space is after chosen coord or we reached the end
            if (index > coord_col and item == []) or index == len(row) - 1:
                # print(index, item)
                # pop off empty space or end
                discarded_tile = row.pop(index)
                # put an empty space before it (avoid indexing error)
                if coord_col - 1 < 0:
                    row.insert(0, [])
                else:
                    row.insert(coord_col - 1, [])
                # reverse back row if moving L or F

                if direction == "L":
                    row.reverse()

                elif direction == "B":
                    for nums, marbles in enumerate(self._board, start=0):
                        self._board[nums][coord_row] = row[nums]

                elif direction == "F":
                    row.reverse()
                    for nums, marbles in enumerate(self._board, start=0):
                        self._board[nums][coord_row] = row[nums]

                #print(row)
                # return what got popped off so we can add to marble count
                return discarded_tile

    def get_marble_count(self):
        """Returns the number of White, Black, and Red marbles on the board as a tuple. (W,B,R)
        """
        white=0
        black=0
        red=0
        for row in self._board:
            for square in row:
                if square=="W":
                    white+=1
                if square=="B":
                    black+=1
                if square=="R":
                    red+=1
        return (white, black, red)

    def get_captured(self, player_name):
        """Returns amount of red marbles captured.
        :param player_name String: name of player to look up red marble count
        """
        try:
            return self._captured[player_name]
        except KeyError:
            return "no player exists"

    def validate_move(self, playername, coordinates, direction):
        """
        :param playername string: name of player
        :param coordinates tuple: coordinates
        :param direction string: direction of pushing
        :return: True or False
        """
        row_coord, column_coord=coordinates[0], coordinates[1]



        # not this player's marble or out of range
        if self.is_players_marble(playername, coordinates) is False:
            return False
        # not this player's turn
        if self._turn is self.get_opposing_player(playername):
            return False
        # game won already
        if self.get_winner() is not None:
            return False
        # no marble at this location
        if self.get_marble(coordinates)=="X":
            return False
        # not this player's marble
        if self.is_players_marble(playername, coordinates) ==False:
            return False


        # get the column as a list for vertical movements
        if direction=="B" or direction=="F":
            proposed_row = self.get_column(column_coord)
            if direction=="F":
                # check if not a empty space and the marbles are the same color (can't push off own marble)
                if [] not in proposed_row[row_coord::-1] and proposed_row[row_coord] == proposed_row[0]:
                    return False
                # attempt to move up but marble blocking below
                if self.get_marble((row_coord + 1, column_coord)) != "X":
                    return False

            elif direction=="B":
                if [] not in proposed_row[row_coord:] and proposed_row[row_coord] == proposed_row[-1]:
                    return False
                # attempt to move down but marble blocking above
                if self.get_marble((row_coord - 1, column_coord)) != "X":
                    return False


        # get the row for horizontal movements
        elif direction=="L" or direction=="R":
            proposed_row=self._board[row_coord]
            if direction=="R":
                # try move right, marble on left
                if self.get_marble((row_coord, column_coord-1)) != "X":
                    return False
                # no empty square to the right and marble same color as end
                if [] not in proposed_row[column_coord:] and proposed_row[column_coord] == proposed_row[-1]:
                    return False
            # try move left, marble on right
            elif direction=="L":
                if self.get_marble((row_coord, column_coord+1))!="X":
                    return False
                # no empty square to left, marbles same color as end
                if [] not in proposed_row[column_coord::-1] and proposed_row[column_coord] == proposed_row[0]:
                    return False


        return True





    def make_move(self, playername, coordinates, direction):
        """Makes a move on the game board. If the move is successful returns True else returns False.
        :param playername String: name of the player making the move
        :param coordinates tuple: coordinates of the marble to be moved
        :param direction String: direction to move the marble at the specified coordinates. Valid directions are L, R, F, B"""

        # '''If the move is being made after the game has been won, or when it's not the player's turn
        #  or if the coordinates provided are not valid or a marble in the coordinates cannot be moved
        #  in the direction specified or it is not the player's marble or for any other invalid conditions return False'''

        # game over, turn is opposing player, no marble at coordinate, not this player's marble at coordinate
        if self.validate_move(playername, coordinates, direction) is False:
            return False

        # update turn after first player plays to be opposite player's turn
        if self._turn is None:
            self._turn = self.get_opposing_player(playername)


# TODO: implement moving the marble row and column logic,
def main():
    testgame = KubaGame(('PlayerA', 'W'), ('PlayerB', 'B'))
    testgame.print_board()
    print(testgame.get_marble((6, 0)))
    print(testgame.get_captured("PlayerA"))
    print(testgame.get_opposing_player("PlayerB"))
    print(testgame.is_players_marble("PlayerB", (5,0)))
    print(testgame.get_marble_count())
    print(testgame.get_column(1))
    print(testgame.validate_move("PlayerA",(0,1), "B"))

if __name__ == '__main__':
    main()