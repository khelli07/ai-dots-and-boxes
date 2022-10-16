from src.Bot import Bot
from src.GameAction import GameAction
from src.GameState import GameState
from src.GenerateChild import ChildrenNode
from src.SquareNode import SquareNode

class LocalSearchBSBot(Bot):
    def get_action(self, state: GameState, player=2) -> GameAction:
        # TODO gimana cara masukin agent sebagai player berapa
        Turn = True if player == 2 else False
        print()
        print("============================")
        print()
        score, action, child = LocalSearchBSBot.minimax(state, Turn, 5, -999999999, 99999999, 5)
        print("EKSPEKTASI ANAK TERBAIK:")
        print("SCORE",score)
        print("AKSI", action)
        print("STATENYA\n",child.board_status)
        return action

    @staticmethod
    def minimax(state: GameState, turn: bool, depth: int, alpha: int, beta:int, maks_anak: int) -> tuple[int, GameAction]:
        if depth == 0 or state.terminal_test()==True:
            return (state.state_value(),GameAction("row", (-1,-1)),state)
        
        bestScore: int = -1
        bestMove: GameAction = GameAction("row", (-1,-1))
        kamus = {}
        if turn==True: 
            children, moves, newSquare = ChildrenNode(state, turn).generate_children(2)
            kamus = {}
            for i in range(len(children)):
                kamus[children[i]] = [moves[i], newSquare[i]]
            children = sorted(children, key=lambda x: x.state_value(), reverse=True)
            children = children[:min(maks_anak,len(children))]
            bestScore = -999999999
            for i in range(len(children)):
                # Ini kalau mau sinkron khelli
                # root = SquareNode(children[i].board_status, children[i].row_status, children[i].col_status, None)
                # temp = root.generate_best_child()
                # score, _ = MinimaxBot.minimax(temp, False, depth-1, alpha, beta)
                if kamus[children[i]][1]:
                    score, _ , a = LocalSearchBSBot.minimax(children[i], True, depth-1, alpha, beta, maks_anak)
                else:
                    score, _, a = LocalSearchBSBot.minimax(children[i], False, depth-1, alpha, beta, maks_anak)
                if score>=bestScore:
                    bestScore = int(max(bestScore, score))
                    bestMove = kamus[children[i]][0]
                    bestChild = a
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
        else: 
            children, moves, newSquare = ChildrenNode(state, turn).generate_children(1)
            kamus = {}
            for i in range(len(children)):
                kamus[children[i]] = [moves[i], newSquare[i]]
            bestScore = 999999999
            children = sorted(children, key=lambda x: x.state_value(), reverse=False)
            children = children[:min(maks_anak,len(children))]

            for i in range(len(children)):
                # Ini kalau mau sinkron khelli
                # root = SquareNode(children[i].board_status, children[i].row_status, children[i].col_status, None)
                # temp = root.generate_best_child()
                # score, _ = MinimaxBot.minimax(temp, False, depth-1, alpha, beta)
                if kamus[children[i]][1]:
                    score, _ , a= LocalSearchBSBot.minimax(children[i], False, depth-1, alpha, beta, maks_anak)
                else:
                    score, _, a = LocalSearchBSBot.minimax(children[i], True, depth-1, alpha, beta, maks_anak)
                if score<=bestScore:
                    bestScore = int(min(bestScore, score))
                    bestMove = kamus[children[i]][0]
                    bestChild = a
                beta = min(beta, score)
                if beta <= alpha:
                    break
        
        return (bestScore, bestMove, bestChild)
