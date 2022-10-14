from src.GameAction import GameAction
from src.GameState import GameState


class ChildrenNode:
    def __init__(self, state: GameState, turn: bool):
        self.state = state
        self.children: list[GameState] = []
        self.moves: list[GameAction] = []
        self.turn = turn

    def generate_children(self):
        for i in range(3):
            for j in range(4):
                if self.state.row_status[j][i] != 1:
                    newChild = GameState(
                        self.state.board_status.copy(), 
                        self.state.row_status.copy(), 
                        self.state.col_status.copy(), 
                        self.turn)
                    newChild.row_status[i][j]=1

                    self.children.append(newChild)
                    self.moves.append(GameAction("row", (i,j)))

                if self.state.col_status[i][j] != 1:
                    newChild = GameState(
                        self.state.board_status.copy(), 
                        self.state.row_status.copy(), 
                        self.state.col_status.copy(), 
                        self.turn)
                    newChild.col_status[j][i]=1

                    self.children.append(newChild)
                    self.moves.append(GameAction("col", (j,i)))
        
        return (self.children, self.moves)