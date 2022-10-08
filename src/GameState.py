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

    # KALAU GILIRAN BOT, TURN ISI TRUE
    # KALAU GILIRAN HUMAN, ISI FALSE AJA

    # Note (khelli)
    # Asumsi sekarang: agent: turn = False
    #                  enemy: turn = True

    # Asumsinya kayan

    def state_value(self, player=2):

        # WEIGHT
        c1 = 10
        c2 = 10

        # ALGORITHM
        my_square = 0
        opponent_square = 0
        almost_square = 0
        for i in self.board_status:
            for j in i:
                if abs(j) == 3:
                    almost_square += 1
                elif j == 4:
                    if player == 2: 
                        my_square += 1 
                    else :
                        opponent_square += 1
                elif j == -4:
                    if player == 2:
                        opponent_square += 1
                    else :
                        my_square += 1 

        square_score = c1 * (my_square - opponent_square)
        almost_score = c2 * almost_square

        #Cek apakah turn nya agent atau bukan
        AgentTurn = True if (player == 2 and not self.player1_turn) or (player == 1 and self.player1_turn) else False

        return square_score + almost_score if AgentTurn else square_score - almost_score
