import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def test_save(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(2, 3, 5)
        g_algo = GraphAlgo(graph)
        g_algo.save_to_json("test1")
        g_algo.load_from_json("test1")
        self.assertEqual(g_algo.graph.v_size(), graph.v_size())
        self.assertEqual(g_algo.graph.e_size(), graph.e_size())
        self.assertEqual(g_algo.graph, graph)
