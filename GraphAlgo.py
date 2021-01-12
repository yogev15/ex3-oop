import queue
import sys
from abc import ABC
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
import json
from GraphInterface import GraphInterface


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'repr_json'):
            return obj.repr_json()
        else:
            return json.JSONEncoder.default(self, obj)


def reset(graph):
    nodes = graph.get_all_v()
    for i in nodes.keys():
        node = graph.getNode(i)
        node.weight = 0.0
        node.tag = False
        node.color = "white"
        node.parent = None


class GraphAlgo(GraphAlgoInterface, ABC):

    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, "r") as f:
            j = json.loads(f.read())
            self.graph = DiGraph()
            self.graph.load_from_json(j)
            return True

    def save_to_json(self, file_name: str) -> bool:
        with open(file_name, "w") as f:
            json.dump(self.graph, f, cls=ComplexEncoder)
            return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph.getNode(id1) is None or self.graph.getNode(id2) is None:
            return -1, None

        if id1 == id2:
            return 0, [id1]

        reset(self.graph)
        self.dijkstra(id1)

        dest = self.graph.getNode(id2)
        if dest.getWeight() == 0:
            return -1, None

        path = list()
        dis = 0
        temp = self.graph.getNode(id1)
        while not dest.__eq__(temp):
            dis += dest.nodesIn[dest.getParent().getKey()]
            path.append(dest.getKey())
            dest = dest.getParent()
        path.append(temp.getKey())
        path.reverse()
        return dis, path

    def connected_component(self, id1: int) -> list:
        raise NotImplementedError

    def connected_components(self) -> List[list]:
        raise NotImplementedError

    def plot_graph(self) -> None:
        raise NotImplementedError

    def dijkstra(self, src):

        q = queue.PriorityQueue()
        node = self.graph.getNode(src)
        node.setTag(True)
        q.put(node)

        while not q.empty():
            node = q.get()
            if node.getColor() == "white":
                node.setColor("grey")
                dic = self.graph.all_out_edges_of_node(node.getKey())
                for k in dic:
                    temp = self.graph.getNode(k)
                    if temp.getWeight() == 0 and src != k:
                        temp.setWeight(node.getWeight() + dic[k])
                        temp.setParent(node)
                    else:
                        w = dic[k] + node.getWeight()
                        if w < temp.getWeight():
                            temp.setWeight(w)
                            temp.setParent(node)

                    if temp.getTag() is False:
                        temp.setTag(True)
                        q.put(temp)
            node.setColor("black")

