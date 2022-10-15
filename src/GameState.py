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

    # HM aku baru kepikiran ternyata konvensinya lebih mudah kalau pakai pendekatan yang kaya di board status
    # Semakin positif statenya, semakin membantu Player2 dan semakin negatif, membantu player 1
    # Jadi buat algo minmax sama local search, kalau sbg player2 ambil child terbesarnya kalau sbg player1 ambil terkecilnya

    def state_value(self):

        # WEIGHT
        c1 = 25
        c2 = 10

        # ALGORITHM
        red_square = 0
        blue_square = 0
        almost_square = 0
        for i in self.board_status:
            for j in i:
                if abs(j) == 3:
                    almost_square += 1
                elif j == 4:
                    red_square += 1
                elif j == -4:
                    blue_square += 1

        square_score = c1 * (red_square - blue_square)
        almost_score = c2 * almost_square

        # KASUS :
        # 1. Sekarang giliran player1. Maka 3/4 square bakal membantu player 1 --> Semakin negatif
        # 2. Sekarang giliran player2. Maka 3/4 square bakal membantu player 2 --> Semakin positif
        return square_score + almost_score if not self.player1_turn else square_score - almost_score

    def terminal_test(self) -> bool:
        for i in self.board_status:
            for j in i:
                if abs(j) != 4:
                    return False
        return True