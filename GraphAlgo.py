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


def reset(graph):
    nodes = graph.get_all_v()
    for i in nodes.keys():
        node = graph.getNode(i)
        node.weight = 0.0
        node.tag = False
        node.color = "white"
        node.parent = None


def reversed_graph(graph):
    nodes = graph.get_all_v()
    neighbours = {}
    reverse = DiGraph()

    for k, v in nodes.items():
        reverse.add_node(k, v.getPos())
        neighbours[k] = graph.all_out_edges_of_node(k)

    for k, v in neighbours.items():
        for i, weight in v.items():
            reverse.add_edge(i, k, weight)

    reset(reverse)
    return reverse


def dfs(key: int, graph: DiGraph) -> list:
    keys = []
    listSCC = [key]
    keys.append(key)
    while listSCC:
        node = listSCC.pop()
        keysList = list(graph.all_out_edges_of_node(node).keys())
        for i in keysList:
            if not graph.getNode(i).getTag():
                listSCC.append(i)
                graph.getNode(i).setTag(True)
                keys.append(i)

    reset(graph)
    return keys


class GraphAlgo(GraphAlgoInterface, ABC):

    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        my_dict = dict()
        graphJson = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                nodes = my_dict["Nodes"]
                edges = my_dict["Edges"]
                for node_dict in nodes:
                    if len(node_dict) < 2:
                        graphJson.add_node(node_dict["id"])
                    else:
                        graphJson.add_node(node_dict["id"], node_dict["pos"])
                for edge_dict in edges:
                    graphJson.add_edge(edge_dict["src"], edge_dict["dest"], edge_dict["w"])
            self.graph = graphJson
            return True

        except IOError as e:
            print(e)
            return False

    #  def load_from_json(self, file_name: str) -> bool:
    #    with open(file_name, "r") as f:
    #        j = json.loads(f.read())
    #        self.graph = DiGraph()
    #        self.graph.load_from_json(j)
    #       return True

    #  def save_to_json(self, file_name: str) -> bool:
    #    with open(file_name, "w") as f:
    #        json.dump(self.graph, f, cls=ComplexEncoder)
    #        return True

    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        edges = []
        for node in self.get_graph().get_all_v().items():
            nodes_dict = dict()
            nodes_dict["id"] = node[1].getKey()
            if len(node) > 1:
                nodes_dict["pos"] = node[1].getPos()
            nodes.append(nodes_dict)
            node_edges = self.get_graph().all_out_edges_of_node(node[1].getKey())
            for edge in node_edges:
                edges_dict = dict()
                edges_dict["src"] = node[1].getKey()
                edges_dict["dest"] = edge
                edges_dict["w"] = node_edges[edge]
                edges.append(edges_dict)
        ans = dict()
        ans["Nodes"] = nodes
        ans["Edges"] = edges

        try:
            with open(file_name, "w") as file:
                json.dump(ans, default=lambda m: m.__dict__, indent=4, fp=file)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.graph.getNode(id1) is None or self.graph.getNode(id2) is None:
            return float('inf'), []

        if id1 == id2:
            return 0, [id1]

        reset(self.graph)
        self.dijkstra(id1)

        dest = self.graph.getNode(id2)
        if dest.getWeight() == 0:
            return float('inf'), []

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

        list1 = dfs(id1, self.graph)
        if list is None:
            return []

        st1 = set(list1)
        reversed_g = reversed_graph(self.graph)
        list2 = dfs(id1, reversed_g)
        if list2 is None:
            return []

        st2 = set(list2)
        return list(st1 & st2)

    def connected_components(self) -> List[list]:
        graph = self.get_graph()
        myList = []
        for i in graph.get_all_v().keys():
            bol = False
            for x in myList:
                if x.__contains__(i):
                    bol = True
            if not bol:
                CC = self.connected_component(i)
                myList.append(CC)
        return myList

    def plot_graph(self) -> None:
        return None

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
