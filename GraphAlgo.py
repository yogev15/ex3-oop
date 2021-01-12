import queue
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


def dijkstra(graph, src):
    if graph is None:
        return
    q = queue.PriorityQueue()
    node = graph.getNode(src)
    q.put(node)



def reset(graph):
    nodes = graph.get_all_v()
    for i in nodes.keys():
        node = graph.getNode(i)
        node.weight = 0.0
        node.tag = 0
        node.color = "white"


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
        dijkstra(self.graph, id1)
        node = self.graph.getNode(id2)
        if node.getWeight(id2) == 0:
            return -1, None

        answer = []
        key = id2

        while key != -1:
            answer.append(key)
            key = path.get(key)

        answer.reverse()
        return node.getWeight, answer


    def connected_component(self, id1: int) -> list:
        raise NotImplementedError

    def connected_components(self) -> List[list]:
        raise NotImplementedError

    def plot_graph(self) -> None:
        raise NotImplementedError
