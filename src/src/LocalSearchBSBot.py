from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.Node import Node
from src.SquareNode import SquareNode

MAX_SCORE = 1000000
MAKS_ANAK = 8


class LocalSearchBSBot(Bot):
    def __init__(self,player = 2):
        self.player = player

    def get_action(self, state: GameState, player=2) -> GameAction:
        turn = True if self.player == 2 else False
        print()
        print("==========================")
        print()
        score, action, child = LocalSearchBSBot.minimax(state, turn, 3, MAKS_ANAK)
        print("EKSPEKTASI ANAK TERBAIK:")
        print("SCORE", score)
        print("STATENYA\n", child.board_status)
        print("ACTION", action)

        return action

    @staticmethod
    def minimax(
        state: GameState, turn: bool, depth: int, maks_anak: int
    ) -> tuple[int, GameAction, GameState]:
        node = Node(
            state.board_status,
            state.row_status,
            state.col_status,
            None,
            None,
            state.player1_turn,
        )
        if depth == 0 or node.terminal_test():
            return (node.state_value(), GameAction("row", (-1, -1)), state)
        
        bestScore: int = -1
        bestMove: GameAction = GameAction("row", (-1, -1))
        bestChild: GameState = state

        if turn:  # Agent's turn, maximizing
            node = node.generate_children()
            bestScore = -MAX_SCORE
            temp = node.children
            anak_terurut = sorted(temp, key=lambda x: x.state_value(), reverse=True)
            node.children = anak_terurut[:min(maks_anak,len(anak_terurut))]
            
            for i in range(len(node.children)):
                child = node.children[i]
                if(depth >= 2):
                    print("DEPTH: ", depth)
                    print(child.board_status)
                    print(child.moves[-1])
                if node.new_square[i]:
                    child = LocalSearchBSBot.get_squared_child(state)
                score, _, a = LocalSearchBSBot.minimax(child, False, depth - 1, MAKS_ANAK)
                if score > bestScore:
                    if(depth >= 2):
                        print(score, bestScore)
                    bestScore = int(score)
                    bestMove = node.children[i].moves[-1]
                    bestChild = a
        else:
            node = node.generate_children()
            bestScore = MAX_SCORE
            temp = node.children
            anak_terurut = sorted(temp, key=lambda x: x.state_value(), reverse=False)
            node.children = anak_terurut[:min(maks_anak,len(anak_terurut))]
            
            for i in range(len(node.children)):
                child = node.children[i]
                if node.new_square[i]:
                    child = LocalSearchBSBot.get_squared_child(state)
                score, _, a = LocalSearchBSBot.minimax(child, True, depth - 1, MAKS_ANAK)
                if score < bestScore:
                    bestScore = int(score)
                    bestMove = node.children[i].moves[-1]
                    bestChild = a

        return (bestScore, bestMove, bestChild)

    @staticmethod
    def get_squared_child(state):
        return SquareNode(
            state.board_status,
            state.row_status,
            state.col_status,
            None,
            None,
            state.player1_turn,
        ).generate_best_child()
