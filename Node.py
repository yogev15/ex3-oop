class Node:

    def __init__(self, key: int, tag: int = -1, pos=None):
        self.key = key
        self.tag = tag
        self.info = 'white'
        self.nodesIn = {}  # (key = int , value = weight)
        self.nodesOut = {}  # (key = int , value = weight)
        self.pos = pos

        def node_toString(self) -> dict:
            dic = {"id": self.key, "location": self.pos}
            return dic

        def get_nodesOut(self) -> dict:
            return self.nodesOut

        def set_pos(self, pos: list):
            self.pos = pos
