import sys

class Node:

    def __init__(self, key: int, tag: int = sys.maxsize, weight: int =0.0, color: str="white", 
        nodesIn: dict={}, nodesOut: dict={}, position: tuple = None):
        self.key = key
        self.tag = tag
        self.weight = weight
        self.color = color
        self.nodesIn = nodesIn  # (key = int , value = weight)
        self.nodesOut = nodesOut  # (key = int , value = weight)
        self.position = position

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

    def __repr__(self):
        return str(self.__dict__)
