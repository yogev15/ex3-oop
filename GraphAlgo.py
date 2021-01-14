import math
import queue
import random
from typing import List
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import json
import matplotlib.pyplot as plt

from GraphInterface import GraphInterface


# A method reset the variable needed to SCC and shortest path
def reset(graph):
    nodes = graph.get_all_v()
    for i in nodes.keys():
        node = graph.getNode(i)
        node.weight = 0.0
        node.tag = False
        node.color = "white"
        node.parent = None


# A method that returns a revered graph of the given graph
# by deleting every edge out of vertex x to Y and connecting the same edge from Y to X
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


# This method helps to check the SCC of a single vertex
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


class GraphAlgo(GraphAlgoInterface):

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
        XV = []
        YV = []
        graph = self.get_graph()
        sum = 10 * graph.v_size()
        nodes = graph.get_all_v().items()

        max_x = 0
        max_y = 0
        min_x = math.inf
        min_y = math.inf
        text = []
        for node in nodes:
            if node[1].getPos() is None:
                self.__generate_random_locations()
            node_x = float(node[1].getPos().split(',')[0])
            node_y = float(node[1].getPos().split(',')[1])
            if node_x > max_x:
                max_x = node_x
            if node_y > max_y:
                max_y = node_y
            if node_x < min_x:
                min_x = node_x
            if node_y < min_y:
                min_y = node_y
        frame_x = max_x - min_x
        frame_y = max_y - min_y
        rad = 1 / 100 * frame_y
        for node in nodes:
            node_x = float(node[1].getPos().split(',')[0])
            node_y = float(node[1].getPos().split(',')[1])
            XV.append(node_x)
            YV.append(node_y)
            text.append([node_x + rad, node_y + rad, node[1].getKey()])
            for edge in graph.all_out_edges_of_node(node[0]):
                dest = graph.get_all_v()[edge]
                dest_x = float(dest.getPos().split(',')[0])
                dest_y = float(dest.getPos().split(',')[1])
                dx = dest_x - node_x
                dy = dest_y - node_y
                line_w = 0.0002 * frame_x
                if line_w > 0.2 * frame_y:
                    line_w = 0.2 * frame_y

                plt.arrow(node_x, node_y, dx, dy, width=line_w, length_includes_head=True, head_width=30 * line_w,
                          head_length=75 * line_w, color='k')

        # plt.text()
        for tex in text:
            plt.text(tex[0], tex[1], tex[2], color='b')

        plt.plot(XV, YV, 'o', color='r')
        plt.grid()
        plt.title("Graph")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

    def __generate_random_locations(self):
        sum = self.get_graph().v_size() + 10
        counter = 1
        graph = self.get_graph()
        for node in graph.get_all_v():
            x = counter / sum
            y = random.random()
            z = 0
            pos = str(x) + ',' + str(y) + ',' + str(z)
            dic = graph.get_all_v()[node].setPos(pos)
            counter += 1

    # an algorithm that helps to check the shortest path from vertex src to every vertex in the graph
    # by running through the graph and changing the variables of the vertexes
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
