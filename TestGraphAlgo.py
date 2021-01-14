import timeit
import unittest

from src.DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def test_save(self):
        graph = DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(2, 3, 5)
        graph.add_edge(1, 3, 2.5)
        graph.add_edge(2, 1, 4)
        graph.add_edge(1, 2, 12.3)

        g_algo = GraphAlgo(graph)
        g_algo.save_to_json("test1")
        g_algo.load_from_json("test1")
        g_algo.connected_components()
        self.assertEqual(g_algo.graph.v_size(), graph.v_size())
        self.assertEqual(g_algo.graph.e_size(), graph.e_size())
        self.assertEqual(g_algo.get_graph(), graph)

    def test_shortest_path(self):
        graph = DiGraph()
        for i in range(8):
            graph.add_node(i)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 4.2)
        graph.add_edge(1, 3, 7.3)
        graph.add_edge(1, 2, 2)
        graph.add_edge(1, 4, 2.5)
        graph.add_edge(0, 2, 12.9)
        graph.add_edge(7, 2, 2.8)
        graph.add_edge(6, 5, 1.4)
        graph.add_edge(5, 0, 13.7)
        graph.add_edge(3, 5, 4.78)
        graph.add_edge(1, 0, 6.9)
        graph.add_edge(0, 1, 1.3)
        graph.add_edge(7, 4, 3.1)
        graph.add_edge(7, 6, 32)
        graph.add_edge(5, 7, 8.12)
        graph.add_edge(6, 2, 0.6)
        graph.add_edge(3, 6, 4.5)
        graph.add_edge(5, 1, 3)
        graph.add_edge(0, 5, 17)
        graph.add_edge(4, 0, 2.678)

        g_algo = GraphAlgo(graph)
        ans = g_algo.shortest_path(1, 3)
        self.assertEqual(ans, (7, [1, 2, 3]))
        ans = g_algo.shortest_path(4, 5)
        self.assertEqual(ans, (15.758000000000003, [4, 0, 1, 2, 3, 5]))
        ans = g_algo.shortest_path(0, 7)
        self.assertEqual(ans, (21.2, [0, 1, 2, 3, 5, 7]))
        ans = g_algo.shortest_path(6, 4)
        self.assertEqual(ans, (6.9, [6, 5, 1, 4]))
        ans = g_algo.shortest_path(2, 0)
        self.assertEqual(ans, (11.878, [2, 3, 4, 0]))

        graph = DiGraph()
        for i in range(3):
            graph.add_node(i)
        graph.add_edge(0, 1, 3)
        g_algo = GraphAlgo(graph)
        ans = g_algo.shortest_path(0, 2)
        self.assertEqual(ans, (float('inf'), []))

    def test_connected_component(self):
        graph = DiGraph()
        for i in range(9):
            graph.add_node(i)
        graph.add_edge(0, 3, 4)
        graph.add_edge(3, 2, 1.3)
        graph.add_edge(2, 0, 2)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 1, 1.3)
        graph.add_edge(4, 5, 2.5)
        graph.add_edge(5, 4, 7)
        graph.add_edge(8, 2, 4)
        graph.add_edge(7, 5, 3)
        graph.add_edge(4, 7, 66)
        g_algo = GraphAlgo(graph)
        ans = g_algo.connected_component(3)
        self.assertEqual(ans, [0, 1, 2, 3])
        ans = g_algo.connected_component(5)
        self.assertEqual(ans, [4, 5, 7])
        ans = g_algo.connected_component(8)
        self.assertEqual(ans, [8])
        ans = g_algo.connected_components()
        self.assertEqual(ans, [[0, 1, 2, 3], [4, 5, 7], [6], [8]])


if __name__ == '__main__':
    unittest.main()

