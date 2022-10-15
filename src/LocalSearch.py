from src.GameState import GameState
from src.RandomBot import RandomBot
from src.SquareNode import SquareNode
from src.Bot import Bot
class LocalSearch(Bot):
    def beamSearch(Node):
        Found = False
        listSuccessor = SquareNode.generate_children()
        print(listSuccessor)
        while(not Found):
            listValueListSuccessor = sorted(listSuccessor, key=lambda x: x.board_status, reverse=True)
            someListSuccessor = listValueListSuccessor[:min(4,len(listSuccessor))]
            listSuccessor = []
            for i in someListSuccessor:
                if i.board_status == 0:
                    Found = True
                else:
                    tempSuccessor = SquareNode.generate_square_moves(i)
                    listSuccessor.append(tempSuccessor)
        return Found