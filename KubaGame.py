# Author: Fahad Awan
# Date: 5/25/2021
# Description:

class KubaGame:
    def __init__(self, player1, player2):
        """Initializer for the Kuba Game. Assigns player marble colors and creates board.
        :param player1 tuple: contains player name and color of the marble that the player is playing R, B, or W
        :param player1 tuple: contains player name and color of the marble that the player is playing R, B, or W
        """
        self._player1=player1
        self._player2=player2