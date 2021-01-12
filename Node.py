class Node:

    def __init__(self, key: int, tag: int = -1, pos: tuple = None):
        self.key = key
        self.tag = tag
        self.weight = 0.0
        self.color = "white"
        self.nodesIn = {}  # (key = int , value = weight)
        self.nodesOut = {}  # (key = int , value = weight)
        self.position = pos

    def __eq__(self, o: object) -> bool:
        return self.key == o.key

    def getKey(self) -> int:
        return self.key

    def getTag(self) -> int:
        return self.tag

    def setTag(self, tag):
        self.tag = tag

    def getPos(self) -> tuple:
        return self.position

    def setPos(self, pos):
        self.position = pos

    def getColor(self) -> str:
        return self.color

    def setColor(self, color):
        self.color = color
