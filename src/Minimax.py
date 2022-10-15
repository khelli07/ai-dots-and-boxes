from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.GenerateChild import ChildrenNode
from src.SquareNode import SquareNode

class MinimaxBot(Bot):
    def get_action(self, state: GameState, player=2) -> GameAction:
        # TODO gimana cara masukin agent sebagai player berapa
        Turn = True if player == 2 else False
        
        _, action = MinimaxBot.minimax(state, Turn, 4, -999999999, 99999999)

        return action

    @staticmethod
    def minimax(state: GameState, turn: bool, depth: int, alpha: int, beta:int) -> tuple[int, GameAction]:
        if depth == 0 or state.terminal_test()==True:
            return (state.state_value(),GameAction("row", (-1,-1)))
        
        bestScore: int = -1
        bestMove: GameAction = GameAction("row", (-1,-1))

        if turn==True: # BERARTI INI MAXIMIZING YA ?
            # Giliran Player 2
            children, moves, newSquare = ChildrenNode(state, turn).generate_children()
            bestScore = -999999999

            for i in range(len(children)):
                # Hitung objective function SETELAH gerak
                if newSquare[i]:
                    score, _ = MinimaxBot.minimax(children[i], True, depth-1, alpha, beta)
                else:
                    score, _ = MinimaxBot.minimax(children[i], False, depth-1, alpha, beta)
                if score>=bestScore:
                    bestScore = int(max(bestScore, score))
                    bestMove = moves[i]
                alpha = max(alpha, score)
                if beta<=alpha:
                    break
        else: # INI MINIMIZING YA?
            # Giliran Player1
            children, moves, newSquare = ChildrenNode(state, turn).generate_children()
            bestScore = 999999999

            for i in range(len(children)):
                # Hitung objective function SETELAH gerak
                if newSquare[i]:
                    score, _ = MinimaxBot.minimax(children[i], False, depth-1, alpha, beta)
                else:
                    score, _ = MinimaxBot.minimax(children[i], True, depth-1, alpha, beta)
                if score<=bestScore:
                    bestScore = int(min(bestScore, score))
                    bestMove = moves[i]
                beta = min(beta, score)
                if beta<=alpha:
                    break
        
        return (bestScore, bestMove)

        
        
        

                

                