import random

import numpy as np

from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.SquareNode import SquareNode
from src.LocalSearch import LocalSearch
from src.Node import Node



class LocalSearchBot(Bot):
    def get_action(self: Node, state: GameState) -> GameAction:
        node_awal = Node(state.board_status.copy(),state.row_status.copy(),state.col_status.copy(),state.player1_turn)
        temp = SquareNode()
        best_node = temp.generate_children(node_awal)
        list_node = temp.children
        print(temp)
        print(list_node)
        print(best_node)
        
        all_row_marked = np.all(state.row_status == 1)
        all_col_marked = np.all(state.col_status == 1)

        if not (all_row_marked or all_col_marked):
            return self.get_random_action(state)
        elif all_row_marked:
            return self.get_random_col_action(state)
        else:
            return self.get_random_row_action(state)

    def get_random_action(self, state: GameState) -> GameAction:
        if random.random() < 0.5:
            return self.get_random_row_action(state)
        else:
            return self.get_random_col_action(state)

    def get_random_row_action(self, state: GameState) -> GameAction:
        position = self.get_random_position_with_zero_value(state.row_status)
        return GameAction("row", position)

    def get_random_position_with_zero_value(self, matrix: np.ndarray):
        [ny, nx] = matrix.shape

        x = -1
        y = -1
        valid = False

        while not valid:
            x = random.randrange(0, nx)
            y = random.randrange(0, ny)
            valid = matrix[y, x] == 0

        return (x, y)

    def get_random_col_action(self, state: GameState) -> GameAction:
        position = self.get_random_position_with_zero_value(state.col_status)
        return GameAction("col", position)

    def heuristic(self, state):
        pass