from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self, nodeSize : int = 0 , edgeSize : int = 0, mc : int = 0 ):
        """
        constructor
        :param nodeSize:
        :param edgeSize:
        :param mc:
        """
        self.nodeSize = nodeSize
        self.edgeSize = edgeSize
        self.mc = mc
        self.graphDict = {} #(node_id, node_data)


    def v_size(self) -> int:
        return self.nodeSize

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.graphDict

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.graphDict.__contains__(id1):
            a = self.graphDict.get(id1)
            return self.graphDict[id1].nodesIn
        else:
            return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.graphDict.__contains__(id1):
            a = self.graphDict.get(id1)
            return self.graphDict[id1].nodesOut
        else:
            return {}

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if weight <=0 or id1==id2:
            return False
        if self.graphDict.__contains__(id1) and self.graphDict.__contains__(id2):
            a = self.graphDict.get(id1)
            b = self.graphDict.get(id2)

        else:
            return False

        if id2 in a.nodesOut:
            a.nodesOut[id2] = weight
            b.nodesIn[id1] = weight
            self.mc += 1
            return True

        if a in self.graphDict.values() and b in self.graphDict.values():
            a.nodesOut[id2] = weight
            b.nodesIn[id1] = weight
            self.edgeSize += 1
            self.mc += 1
            return True


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.graphDict.get(node_id):
            return False
        a = Node(node_id)
        self.graphDict[node_id] = a
        self.nodeSize += 1
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.graphDict.__contains__(node_id):
            node = self.graphDict.get(node_id)
            for key in node.nodesOut:
                temp = self.graphDict.get(key)
                temp.nodesIn.pop(node_id)
                self.mc += 1
                self.edgeSize -= 1

            for key in node.nodesIn:
                temp = self.graphDict.get(key)
                temp.nodesOut.pop(node_id)
                self.mc += 1
                self.edgeSize -= 1


            self.graphDict.pop(node_id)
            self.mc += 1
            self.nodeSize -= 1
            return True
        return False


    def toString (self):
        return "v size is "+self.nodeSize+" , e size is "+self.edgeSize


    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self.graphDict.__contains__(node_id1) and self.graphDict.__contains__(node_id2) and node_id1 != node_id2:

            a = self.graphDict.get(node_id1)
            b = self.graphDict.get(node_id2)
            if a.nodesOut.__contains__(node_id2):
                del a.nodesOut[node_id2]
                del b.nodesIn[node_id1]
                self.edgeSize -= 1
                self.mc += 1
                return True

        return False





