from src.GameAction import GameAction
from src.Node import Node


class SquareNode(Node):
    """
    Helps to return best child of a node if agent/enemy has > 1 move
    e.g. if agent/enemy made a square

    best_child will return SquareNode which has an attribute called "moves"
    "moves" will be a list of GameAction to be taken by agent/enemy to reach best_child
    """

    def generate_best_child(self):
        last_best = best_child = SquareNode.generate_square_moves(self)
        if last_best.children:
            max_score, best_child = (
                last_best.children[0].state_value(),
                last_best.children[0],
            )
            for child in last_best.children:
                score = child.state_value()
                if not self.player1_turn:
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
        if new_square and node.children:
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
                        not self.player1_turn,
                    )
                    has_new_square = new_row.update(i, j, True)
                    self.new_square.append(has_new_square)
                    if has_new_square:
                        new_row.player1_turn = self.player1_turn
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
                        not self.player1_turn,
                    )

                    has_new_square = new_col.update(j, i, False)
                    self.new_square.append(has_new_square)
                    if has_new_square:
                        new_col.player1_turn = self.player1_turn
                        self.children.append(new_col)
                        return True
                    else:
                        no_new_square.append(new_col)

        self.children = no_new_square
        return False


# import numpy as np

# CASE 1: if agent can claim all square until the game ends
# board_status = np.array([[0, -1, -3], [2, 2, 2], [-3, -2, -2]])
# row_status = np.array([[0, 0, 1], [0, 0, 0], [1, 1, 0], [1, 1, 1]])
# col_status = np.array([[0, 0, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]])


# CASE 2: if agent can only claim several squares and the game still continues
# board_status = np.array([[0, 1, -3], [0, -1, -2], [0, -1, 3]])
# row_status = np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0], [0, 0, 1]])
# col_status = np.array([[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]])

# CASE 3: initial  game
# board_status = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
# row_status = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]])
# col_status = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

# root = SquareNode(board_status, row_status, col_status, None, player1_turn=False)
# best_child = root.generate_best_child()
# print(best_child.moves)
# print(best_child.board_status)
# print(best_child.row_status)
# print(best_child.col_status)
