from src.GameAction import GameAction
from src.GameState import GameState


class ChildrenNode:
    def __init__(self, state: GameState, turn: bool):
        self.state = state
        self.children: list[GameState] = []
        self.moves: list[GameAction] = []
        self.turn = turn
        self.newSquare : list[bool] = []

    def generate_children(self, player = 2):
        # kalo skrg giliran player1, nanti anaknya giliran player 2 trus viceversa
        if player == 2:
            next_player1turn = True
        else :
            next_player1turn = False
        for i in range(3):
            for j in range(4):
                if self.state.row_status[j][i] != 1:
                    newChild = GameState(
                        self.state.board_status.copy(), 
                        self.state.row_status.copy(), 
                        self.state.col_status.copy(), 
                        next_player1turn)
                    newChild.row_status[j][i]=1

                    # CEK ATASNYA TERBENTUK KOTAK APA ENGGA
                    kotakbaru = False
                    if j != 0:
                        if self.state.row_status[j-1][i] == 1 and self.state.col_status[j-1][i] == 1 and self.state.col_status[j-1][i+1] == 1:
                            kotakbaru = True
                        if player == 2:
                            newChild.board_status[j-1][i] = (abs(self.state.board_status[j-1][i]))+1
                        else : 
                            newChild.board_status[j-1][i] = -1*((abs(self.state.board_status[j-1][i]))+1)

                    #CEK BAWAHNYA TERBENTUK KOTAK APA ENGGA
                    if j != 3:
                        if self.state.row_status[j+1][i] == 1 and self.state.col_status[j][i] == 1 and self.state.col_status[j][i+1] == 1:
                            kotakbaru = True
                        if player == 2:
                            newChild.board_status[j][i] = (abs(self.state.board_status[j][i]))+1
                        else : 
                            newChild.board_status[j][i] = -1*((abs(self.state.board_status[j][i]))+1)

                    self.children.append(newChild)
                    self.moves.append(GameAction("row", (i,j)))
                    self.newSquare.append(kotakbaru)

                if self.state.col_status[i][j] != 1:
                    newChild = GameState(
                        self.state.board_status.copy(), 
                        self.state.row_status.copy(), 
                        self.state.col_status.copy(), 
                        next_player1turn)
                    newChild.col_status[i][j]=1

                    #CEK KIRI TERBENTUK KOTAK APA ENGGA
                    kotakbaru = False
                    if j != 0:
                        if self.state.col_status[i][j-1] == 1 and self.state.row_status[i][j-1] == 1 and self.state.row_status[i+1][j-1] == 1:
                            kotakbaru = True
                        if player == 2:
                            newChild.board_status[i][j-1] = (abs(self.state.board_status[i][j-1]))+1
                        else : 
                            newChild.board_status[i][j-1] = -1*((abs(self.state.board_status[i][j-1]))+1)

                    #CEK KANAN TERBENTUK KOTAK APA ENGGA
                    if j != 3:
                        if self.state.col_status[i][j+1] == 1 and self.state.row_status[i][j] == 1 and self.state.row_status[i+1][j] == 1:
                            kotakbaru = True
                        if player == 2:
                            newChild.board_status[i][j] = (abs(self.state.board_status[i][j]))+1
                        else : 
                            newChild.board_status[i][j] = -1*((abs(self.state.board_status[i][j]))+1)

                    self.children.append(newChild)
                    self.moves.append(GameAction("col", (j,i)))
                    self.newSquare.append(kotakbaru)
        
        return (self.children, self.moves, self.newSquare)