import unittest
from DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
        graph = DiGraph()
        self.assertEqual(graph.v_size(), 0)
        graph.add_node(0)
        self.assertEqual(graph.v_size(), 1)
        for i in range(1, 10):
            graph.add_node(i)
        self.assertEqual(graph.v_size(), 10)
        graph.remove_node(9)
        self.assertEqual(graph.v_size(), 9)
        graph.remove_node(9)
        self.assertEqual(graph.v_size(), 9)
        graph.remove_node(15)
        self.assertEqual(graph.v_size(), 9)

    def test_e_size(self):
        graph = DiGraph()
        for i in range(1, 5):
            graph.add_node(i)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 5)
        graph.add_edge(2, 3, 1)
        graph.add_edge(4, 2, 7.5)
        self.assertEqual(graph.e_size(), 4)
        graph.add_edge(4, 2, 5)
        self.assertEqual(graph.e_size(), 4)
        graph.add_edge(4, 4, 5)
        self.assertEqual(graph.e_size(), 4)
        bol = graph.add_edge(8, 2, 1)  # 8 is not a node in the graph
        self.assertFalse(bol)
        self.assertEqual(graph.e_size(), 4)
        graph.remove_edge(1, 2)
        self.assertEqual(graph.e_size(), 3)
        graph.remove_edge(1, 2)
        self.assertEqual(graph.e_size(), 3)
        graph.remove_edge(8, 1)
        graph.remove_edge(2, 2)
        self.assertEqual(graph.e_size(), 3)

    def test_get_all_v(self):
        graph = DiGraph()
        expected_dict = {}
        for i in range(1, 5):
            graph.add_node(i)
            expected_dict[i] = graph.graphDict.get(i)
        self.assertEqual(graph.get_all_v(), expected_dict)

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        for i in range(1, 5):
            graph.add_node(i)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 5)
        graph.add_edge(2, 3, 1)
        graph.add_edge(4, 2, 7.5)
        expected_dict = {1: 2, 4: 7.5}
        self.assertEqual(graph.all_in_edges_of_node(2), expected_dict)
        self.assertEqual(graph.all_in_edges_of_node(7), {})

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        for i in range(1, 5):
            graph.add_node(i)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 5)
        graph.add_edge(2, 3, 1)
        graph.add_edge(4, 2, 7.5)
        expected_dict = {1: 5,  3: 1}
        self.assertEqual(graph.all_out_edges_of_node(2), expected_dict)
        self.assertEqual(graph.all_out_edges_of_node(3), {})

    def test_get_mc(self):
        graph = DiGraph()
        for i in range(1, 101):
            graph.add_node(i)
        self.assertEqual(graph.mc, 100)
        graph.remove_edge(1, 100)
        self.assertEqual(graph.mc, 100)
        graph.add_edge(1, 2, 3)
        self.assertEqual(graph.mc, 101)
        graph.remove_edge(1, 2)
        self.assertEqual(graph.mc, 102)
        graph.add_node(3)
        self.assertEqual(graph.mc, 102)
        graph.remove_node(105)
        self.assertEqual(graph.mc, 102)
        graph.add_edge(2, 4, 2)
        graph.add_edge(2, 5, 2)
        graph.add_edge(5, 2, 3)
        graph.add_edge(80, 81, 1)
        self.assertEqual(graph.mc, 106)
        graph.remove_node(2)  # remove 3 edges and 1 node
        self.assertEqual(graph.mc, 110)
        out_from_node = graph.all_out_edges_of_node(5)
        dict_keys = {}
        self.assertEqual(out_from_node, dict_keys)

    def test_add_remove_node(self):
        graph = DiGraph()
        for i in range(1, 5):
            graph.add_node(i)
        bol = graph.add_node(1)
        self.assertFalse(bol)
        bol = graph.add_node(6)
        self.assertTrue(bol)
        self.assertEqual(graph.v_size(), 5)
        bol = graph.remove_node(1)
        self.assertEqual(graph.v_size(), 4)
        self.assertTrue(bol)
        bol = graph.remove_node(1)
        self.assertEqual(graph.v_size(), 4)
        self.assertFalse(bol)
        bol = graph.remove_node(5)
        self.assertEqual(graph.v_size(), 4)
        self.assertFalse(bol)

    def test_add_remove_edge(self):
        graph = DiGraph()
        for i in range(1, 5):
            graph.add_node(i)
        bol = graph.add_edge(1, 2, 2)
        self.assertEqual(graph.e_size(), 1)
        graph.add_edge(1, 4, 3)
        self.assertEqual(graph.e_size(), 2)
        self.assertTrue(bol)
        bol = graph.add_edge(6, 1, 30)
        self.assertFalse(bol)
        bol = graph.add_edge(1, 1, 2)
        self.assertFalse(bol)
        self.assertEqual(graph.e_size(), 2)
        bol = graph.remove_edge(1, 1)
        self.assertFalse(bol)
        self.assertEqual(graph.e_size(), 2)
        bol = graph.remove_edge(1, 2)
        self.assertTrue(bol)
        self.assertEqual(graph.e_size(), 1)
        bol = graph.remove_edge(1, 5)
        self.assertFalse(bol)
        self.assertEqual(graph.e_size(), 1)
        expected_dict = {4: 3}
        self.assertEqual(graph.all_out_edges_of_node(1), expected_dict)


if __name__ == '__main__':
    unittest.main()
