from abc import ABC
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
import json
from GraphInterface import GraphInterface
from Node import Node


class GraphAlgo(GraphAlgoInterface, ABC):

    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        g = DiGraph()
        try:
            with open(file_name, "r") as f:
                details = json.load(f)
                graphDict = details.get("Nodes")
                nodesOut = details.get("Edges")
                for dic in graphDict:
                    key = dic.get("id")
                    pos = dic.get("location")
                    g.add_node(key)
                    g.add_node(key).set_pos(pos)
                for dic in nodesOut:
                    g.add_edge(dic.get("src"), dic.get("dest"), dic.get("w"))
                    self.graph = g
                    return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                json.dump(self.graph, default=lambda m: m.graph_toString, indent=4, fp=file)
                return True
        except IOError as e:
            print("error")
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        raise NotImplementedError

    def connected_component(self, id1: int) -> list:

        raise NotImplementedError

    def connected_components(self) -> List[list]:

        raise NotImplementedError

    def plot_graph(self) -> None:

        raise NotImplementedError