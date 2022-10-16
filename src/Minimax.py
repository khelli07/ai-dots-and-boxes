from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.GenerateChild import ChildrenNode
from src.SquareNode import SquareNode

class MinimaxBot(Bot):
    def get_action(self, state: GameState, player=2) -> GameAction:
        turn = True if (player == 2 and state.player1_turn==False) or (player==1 and state.player1_turn==True) else False
        
        score, action, child = MinimaxBot.minimax(state, turn, 5, -999999999, 99999999)
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
            children, moves, newSquare = ChildrenNode(state, turn).generate_children(2)
            bestScore = -999999999
            for i in range(len(children)):
                # Ini kalau mau sinkron khelli
                # root = SquareNode(children[i].board_status, children[i].row_status, children[i].col_status, None)
                # temp = root.generate_best_child()
                # score, _ = MinimaxBot.minimax(temp, False, depth-1, alpha, beta)
                if newSquare[i]:
                    score, _ , a = MinimaxBot.minimax(children[i], True, depth-1, alpha, beta)
                else:
                    score, _, a = MinimaxBot.minimax(children[i], False, depth-1, alpha, beta)
                if score>=bestScore:
                    bestScore = int(max(bestScore, score))
                    bestMove = moves[i]
                    bestChild = a
                alpha = max(alpha, score)
                if beta<=alpha:
                    break
        else: # INI MINIMIZING YA?
            # Giliran Player1
            children, moves, newSquare = ChildrenNode(state, turn).generate_children(1)
            bestScore = 999999999

            for i in range(len(children)):
                # Ini kalau mau sinkron khelli
                # root = SquareNode(children[i].board_status, children[i].row_status, children[i].col_status, None)
                # temp = root.generate_best_child()
                # score, _ = MinimaxBot.minimax(temp, False, depth-1, alpha, beta)
                if newSquare[i]:
                    score, _ , a= MinimaxBot.minimax(children[i], False, depth-1, alpha, beta)
                else:
                    score, _, a = MinimaxBot.minimax(children[i], True, depth-1, alpha, beta)
                if score<=bestScore:
                    bestScore = int(min(bestScore, score))
                    bestMove = moves[i]
                    bestChild = a
                beta = min(beta, score)
                if beta<=alpha:
                    break
        
        return (bestScore, bestMove, bestChild)

        
        
        

                

                