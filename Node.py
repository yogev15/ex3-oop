
class Node:
    def __init__(self, key: int, tag: bool = False, weight: int = 0.0, color: str = "white",
                 nodesIn: dict = None, nodesOut: dict = None, position: tuple = None, parent=None):
        self.key = key
        self.tag = tag
        self.weight = weight
        self.color = color
        if nodesIn is None:
            self.nodesIn = {}
        else:
            self.nodesIn = nodesIn  # (key = int , value = weight)
        if nodesOut is None:
            self.nodesOut = {}
        else:
            self.nodesOut = nodesOut  # (key = int , value = weight)
        self.position = position
        self.parent = parent

    def getNodesOut(self) -> dict:
        return self.nodesOut

    def getKey(self) -> int:
        return self.key

    def getTag(self) -> bool:
        return self.tag

    def setTag(self, tag):
        self.tag = tag

    def getPos(self) -> tuple:
        return self.position

    def setPos(self, p):
        self.position = p

    def getColor(self) -> str:
        return self.color

    def setColor(self, c):
        self.color = c

    def getWeight(self) -> float:
        return self.weight

    def setWeight(self, w):
        self.weight = w

    def repr_json(self):
        return self.__dict__

    def getParent(self):
        return self.parent

    def setParent(self, p):
        self.parent = p

    def __repr__(self):
        return str(self.__dict__)

    def __eq__(self, other) -> bool:
        return self.key == other.key and self.position == other.position

    def __lt__(self, other):
        p = (self.weight , self.key)
        h = (other.getWeight(), other.getKey())
        return p < h
