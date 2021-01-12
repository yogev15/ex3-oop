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

    def test_shortest_path(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        graph.add_edge(2, 3, 5)
        graph.add_edge(1, 3, 2)
        graph.add_edge(3, 7, 4.2)
        graph.add_edge(7, 9, 12.3)
        graph.add_edge(1, 5, 2.5)
        graph.add_edge(5, 6, 1)
        graph.add_edge(6, 8, 9)
        graph.add_edge(8, 0, 1.7)
        graph.add_edge(9, 6, 5.6)
        graph.add_edge(0, 1, 4.3)
        g_algo = GraphAlgo(graph)
        ans = g_algo.shortest_path(1, 3)
        self.assertEqual(ans, {2, [1, 3]})


if __name__ == '__main__':
    unittest.main()
