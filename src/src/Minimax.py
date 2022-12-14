from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.Node import Node
from src.SquareNode import SquareNode

MAX_SCORE = 1000000


class MinimaxBot(Bot):
    def __init__(self,player = 2):
        self.player = player
        
    def get_action(self, state: GameState) -> GameAction:
        turn = True if self.player == 2 else False
        #INI BIAR DIA KALAU INITNYA 2 SEBAGAI PLAYER 2 --> MAX, KALAU INIT SBG PLAYER 1 --> MIN

        score, action = MinimaxBot.minimax(state, turn, 4, -MAX_SCORE, MAX_SCORE)

        return action

    @staticmethod
    def minimax(
        state: GameState, turn: bool, depth: int, alpha: int, beta: int
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

            return (node.state_value(), GameAction("row", (-1, -1)))

        bestScore: int = -1
        bestMove: GameAction = GameAction("row", (-1, -1))
        bestChild: GameState = state

        if turn:  # Agent's turn, maximizing
            node = node.generate_children()
            bestScore = -MAX_SCORE
            for i in range(len(node.children)):
                child = node.children[i]
                if node.new_square[i]:
                    child = MinimaxBot.get_squared_child(state)
                score, _ = MinimaxBot.minimax(child, False, depth - 1, alpha, beta)
                if score > bestScore:
                    bestScore = int(score)
                    bestMove = node.children[i].moves[-1]
                alpha = max(alpha, score)
                if beta < alpha:
                    break
        else:
            node = node.generate_children()
            bestScore = MAX_SCORE

            for i in range(len(node.children)):
                child = node.children[i]
                if node.new_square[i]:
                    child = MinimaxBot.get_squared_child(state)
                score, _ = MinimaxBot.minimax(child, True, depth - 1, alpha, beta)
                if score < bestScore:
                    bestScore = int(score)
                    bestMove = node.children[i].moves[-1]
                beta = min(beta, score)
                if beta < alpha:
                    break

        return (bestScore, bestMove)

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
