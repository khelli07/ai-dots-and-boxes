import typing

from src.GameAction import GameAction
from src.GameState import GameState


class Node(GameState):
    def __init__(
        self,
        board_status,
        row_status,
        col_status,
        move,
        parent=None,
        player1_turn=True,
    ):
        super().__init__(board_status, row_status, col_status, player1_turn)
        self.parent = parent
        self.children: typing.List[Node] = []
        self.new_square: typing.List[bool] = []
        if parent is None:
            self.moves = []
        else:
            self.moves = parent.moves + [move]

    def generate_children(self):
        for i in range(3):
            for j in range(4):
                if self.row_status[j][i] != 1:
                    new_row = Node(
                        self.board_status.copy(),
                        self.row_status.copy(),
                        self.col_status.copy(),
                        GameAction("row", (i, j)),
                        self,
                        not self.player1_turn,
                    )
                    has_square = new_row.update(i, j, True)
                    self.children.append(new_row)
                    self.new_square.append(has_square)

                if self.col_status[i][j] != 1:
                    new_col = Node(
                        self.board_status.copy(),
                        self.row_status.copy(),
                        self.col_status.copy(),
                        GameAction("col", (j, i)),
                        self,
                        not self.player1_turn,
                    )
                    has_square = new_col.update(j, i, False)
                    self.children.append(new_col)
                    self.new_square.append(has_square)

        return self

    def update(self, x, y, is_row):
        val = 1
        playerModifier = 1
        if not self.player1_turn:
            playerModifier = -1

        is_square_created = False
        if y < 3 and x < 3:
            self.board_status[y][x] = (
                abs(self.board_status[y][x]) + val
            ) * playerModifier
            if abs(self.board_status[y][x]) == 4:
                is_square_created = True

        if is_row:
            self.row_status[y][x] = 1
            if y >= 1:
                self.board_status[y - 1][x] = (
                    abs(self.board_status[y - 1][x]) + val
                ) * playerModifier
                if abs(self.board_status[y - 1][x]) == 4:
                    is_square_created = True

        else:
            self.col_status[y][x] = 1
            if x >= 1:
                self.board_status[y][x - 1] = (
                    abs(self.board_status[y][x - 1]) + val
                ) * playerModifier
                if abs(self.board_status[y][x - 1]) == 4:
                    is_square_created = True

        return is_square_created

    def state_value(self):
        """
        Note : Positif --> Membantu player 2, Negatif --> Membantu player 1
        """
            
        # WEIGHT
        c1 = 100
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

        result = square_score + almost_score if not self.player1_turn else square_score - almost_score
        return result

    def terminal_test(self) -> bool:
        for i in self.board_status:
            for j in i:
                if abs(j) != 4:
                    return False
        return True