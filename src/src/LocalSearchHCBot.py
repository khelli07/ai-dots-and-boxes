import random
from xmlrpc.client import Boolean

import numpy as np

from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.SquareNode import SquareNode
from src.GenerateChild import ChildrenNode
from src.Node import Node

class LocalSearchHCBot(Bot):
    def get_action(self: Node, state: GameState, player=2) -> GameAction:
        children, moves, _ = ChildrenNode(state, True).generate_children(2)
        index = 0
        temp_value = -9999
        print()
        print("======================================================")
        print()
        print("INI STATE MULA-MULA")
        print(state.board_status)
        for i in range(len(children)):
            node = Node(
                children[i].board_status,
                children[i].row_status,
                children[i].col_status,
                moves[i],
                state,
                children[i].player1_turn,
            )
            if(temp_value < node.state_value()):
                temp_value = node.state_value()
                index = i 
        return moves[index]