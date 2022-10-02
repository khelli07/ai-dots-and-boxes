from typing import NamedTuple

from numpy import ndarray


class GameState(NamedTuple):
    """
    board_status: int[][]
        For each element, if its absolute element is four, then
        the square has been taken by a player. If element's sign
        is negative, then it has been taken by player 1. Otherwise,
        it has been taken by player 2.
        Access: board_status[y, x]

    row_status: int[][]
        Represent the horizontal line mark status: 1 for marked, 0 for not.
        Access: row_status[y, x]

    col_status: int[][]
        Represent the vertical line mark status: 1 for marked, 0 for not.
        Access: col_status[y, x]

    player1_turn: bool
        True if it is player 1 turn, False for player 2.
    """

    board_status: ndarray
    row_status: ndarray
    col_status: ndarray
    player1_turn: bool

    # KALAU GILIRAN BOT, TURN ISI TRUE
    # KALAU GILIRAN HUMAN, ISI FALSE AJA
    def State_Value(self,turn):

        # WEIGHT
        c1 = 2
        c2 = 3

        #ALGORITHM
        my_square = 0
        opponent_square = 0
        almost_square = 0
        for i in self.board_status :
            for j in i :
                if abs(j) == 3:
                    almost_square += 1
                elif j == 4:
                    my_square += 1
                elif j == -4:
                    opponent_square += 1

        return c1*(my_square - opponent_square) + c2*almost_square if turn else c1*(my_square - opponent_square) - c2*almost_square

