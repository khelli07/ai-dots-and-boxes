from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.GenerateChild import ChildrenNode
from src.SquareNode import SquareNode
from src.Node import Node

class MinimaxBot(Bot):
    def get_action(self, state: GameState, player=2) -> GameAction:
        turn = True if (player == 2) else False
        
        score, action, child = MinimaxBot.minimax(state, turn, 4, -999999999, 99999999)
        print("EKSPEKTASI ANAK TERBAIK:")
        print("SCORE",score)
        print("STATENYA\n",child.board_status)

        return action

    @staticmethod
    def minimax(state: GameState, turn: bool, depth: int, alpha: int, beta:int) -> tuple[int, GameAction, GameState]:
        if depth == 0 or state.terminal_test()==True:
            return (state.state_value(),GameAction("row", (-1,-1)),state)
        
        bestScore: int = -1
        bestMove: GameAction = GameAction("row", (-1,-1))
        bestChild: GameState = state

        if turn==True: # BERARTI INI MAXIMIZING YA ?
            # Giliran Player 2
            # children, moves, newSquare = ChildrenNode(state, turn).generate_children(2)
            node = Node(state.board_status, state.row_status, state.col_status, None, None, state.player1_turn) 
            node.generate_children()
            bestScore = -999999999
            for i in range(len(node.children)):
                if node.new_square[i]:
                    squared_best = SquareNode(state.board_status, state.row_status, state.col_status, None, None, state.player1_turn)
                    score, _ , a = MinimaxBot.minimax(squared_best, True, depth-1, alpha, beta)
                else:
                    score, _, a = MinimaxBot.minimax(node.children[i], False, depth-1, alpha, beta)
                if score > bestScore:
                    bestScore = int(score)
                    bestMove = node.children[i].moves[-1]
                    bestChild = a
                alpha = max(alpha, score)
                if beta < alpha:
                    break
        else: # INI MINIMIZING YA?
            # Giliran Player1
            # children, moves, newSquare = ChildrenNode(state, turn).generate_children(1)
            node = Node(state.board_status, state.row_status, state.col_status, None, None, state.player1_turn) 
            node.generate_children()
            bestScore = 999999999

            for i in range(len(node.children)):
                if node.new_square[i]:
                    squared_best = SquareNode(state.board_status, state.row_status, state.col_status, None, None, state.player1_turn)
                    score, _ , a= MinimaxBot.minimax(squared_best, False, depth-1, alpha, beta)
                else:
                    score, _, a = MinimaxBot.minimax(node.children[i], True, depth-1, alpha, beta)
                if score < bestScore:
                    bestScore = int(score)
                    bestMove = node.children[i].moves[-1]
                    bestChild = a
                beta = min(beta, score)
                if beta < alpha:
                    break
        
        return (bestScore, bestMove, bestChild)

        
        
        

                

                