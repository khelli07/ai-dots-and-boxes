from numpy import ndarray


class GameState:
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

    def __init__(self, board_status, row_status, col_status, player1_turn):
        self.board_status = board_status
        self.row_status = row_status
        self.col_status = col_status
        self.player1_turn = player1_turn