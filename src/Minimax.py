from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from GenerateChild import ChildrenNode

class MinimaxBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        # TODO gimana cara masukin agent sebagai player berapa
        _, action = MinimaxBot.minimax(state, state.player1_turn, 4, -999999999, 99999999)
        return action

    @staticmethod
    def minimax(state: GameState, turn: bool, depth: int, alpha: int, beta:int) -> tuple[int, GameAction]:
        if depth==0 or state.terminal_test()==True:
            return (state.state_value(turn),GameAction("row", (-1,-1)))
        
        bestScore: int = -1
        bestMove: GameAction = GameAction("row", (-1,-1))

        if turn==False:
            # Giliran agent
            children, moves = ChildrenNode(state, turn).generate_children()
            bestScore = -999999999

            for i in range(len(children)):
                # Hitung objective function SETELAH gerak
                score, _ = MinimaxBot.minimax(children[i], True, depth-1, alpha, beta)
                if score>bestScore:
                    bestScore = int(max(bestScore, score))
                    bestMove = moves[i]
                alpha = max(alpha, score)
                if beta<=alpha:
                    break
        elif turn==False:
            # Giliran agent
            children, moves = ChildrenNode(state, turn).generate_children()
            bestScore = 999999999

            for i in range(len(children)):
                # Hitung objective function SETELAH gerak
                score, _ = MinimaxBot.minimax(children[i], False, depth-1, alpha, beta)
                if score<bestScore:
                    bestScore = int(min(bestScore, score))
                    bestMove = moves[i]
                beta = min(beta, score)
                if beta<=alpha:
                    break
        
        return (bestScore, bestMove)
        
        
        

                

                