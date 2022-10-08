import typing

from GameAction import GameAction
from GameState import GameState


class SquareNode(GameState):
    """
    Helps to return best child of a node if agent/enemy has > 1 move
    e.g. if agent/enemy made a square

    Usage:
    root = SquareNode(board_status, row_status, col_status, None)
    best_child = root.generate_best_child(is_enemy=False)

    best_child will return SquareNode which has an attribute called "moves"
    "moves" will be a list of GameAction to be taken by agent/enemy to reach best_child
    """

    def __init__(
        self, board_status, row_status, col_status, move: GameAction, parent=None
    ):
        super().__init__(board_status, row_status, col_status, True)
        self.parent = parent
        self.children: typing.List[SquareNode] = []
        if parent is None:
            self.moves = [move]
        else:
            self.moves = parent.moves + [move]

    def generate_best_child(self, is_enemy=False):
        last_best = best_child = SquareNode.generate_square_moves(self)
        if last_best.children:
            max_score, best_child = (
                last_best.children[0].state_value(is_enemy),
                last_best.children[0],
            )
            for child in last_best.children:
                score = child.state_value(is_enemy)
                if not is_enemy:
                    if score > max_score:
                        max_score = score
                        best_child = child
                else:
                    if score < max_score:
                        max_score = score
                        best_child = child

        return best_child

    @staticmethod
    def generate_square_moves(node):
        """
        Recursive function to get every square possible
        """
        new_square = node.generate_children()
        # print(new_square)
        if new_square:
            return SquareNode.generate_square_moves(node.children[0])
        else:
            return node

    def generate_children(self):
        """
        If a child has one square, the function will immidiately return that one child
            i.e. if this node can claim a square, this node's children will be only 1
        else, it will return all possible children with no squares
        """
        no_new_square = []

        for i in range(3):
            for j in range(4):
                if self.row_status[j][i] != 1:
                    new_row = SquareNode(
                        self.board_status.copy(),
                        self.row_status.copy(),
                        self.col_status.copy(),
                        GameAction("row", (i, j)),
                        self,
                    )
                    has_new_square = new_row.update(i, j, True)
                    if has_new_square:
                        self.children.append(new_row)
                        return True
                    else:
                        no_new_square.append(new_row)

                if self.col_status[i][j] != 1:
                    new_col = SquareNode(
                        self.board_status.copy(),
                        self.row_status.copy(),
                        self.col_status.copy(),
                        GameAction("col", (j, i)),
                        self,
                    )

                    has_new_square = new_col.update(j, i, False)
                    if has_new_square:
                        self.children.append(new_col)
                        return True
                    else:
                        no_new_square.append(new_col)

        self.children = no_new_square
        return False

    def update(self, x, y, is_row, is_enemy=False):
        val = 1
        playerModifier = 1
        if not is_enemy:
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


# import numpy as np

# CASE 1: if agent can claim all square until the game ends
# board_status = np.array([[-3, 3, -3], [-2, 3, -2], [-2, 2, 2]])
# row_status = np.array([[1, 1, 1], [0, 0, 0], [0, 1, 0], [1, 1, 1]])
# col_status = np.array([[1, 1, 1, 1], [1, 1, 1, 1], [1, 0, 0, 1]])

# CASE 2: if agent can only claim several squares and the game still continues
# board_status = np.array([[0, 1, -3], [0, -1, -2], [0, -1, 3]])
# row_status = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 1]])
# col_status = np.array([[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]])

# root = SquareNode(board_status, row_status, col_status, None)
# best_child = root.generate_best_child(False)
# print(best_child.moves)
# print(best_child.board_status)
# print(best_child.row_status)
# print(best_child.col_status)
