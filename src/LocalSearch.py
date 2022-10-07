from src.GameState import GameState

""" class LocalSearch():
    def beamSearch(Node):
        Found = False
        listSuccessor = []
        if(not findSuccessor(Node)):
            Found = True
        else:
            listSuccessor = findSuccessor(Node)
        while(!Found):
            listSuccessor.sort()
            someListSuccessor = listSuccessor[:min(4,len(listSuccessor))]
            listSuccessor = []
            for i in someListSuccessor:
                if score(i) === 0:
                    Found = True
                else:
                    tempSuccessor = findSuccessor(i)
                    listSuccessor.append(tempSuccessor)
        return Found """