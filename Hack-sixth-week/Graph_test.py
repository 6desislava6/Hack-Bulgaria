import unittest
from Graph import DirectedGraph
from Graph import Already_there
from Graph import Cant_follow_yourself


class Graph_test(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_add_node(self):
        self.graph.add_node('A')
        self.assertTrue('A' in self.graph.nodes)
        with self.assertRaises(Already_there):
            self.graph.add_node('A')

    def test_add_edge(self):
        self.graph.add_edge('A', 'B')
        self.assertEqual(self.graph.nodes['A'], set('B'))
        self.assertEqual(self.graph.nodes['B'], set())
        with self.assertRaises(Cant_follow_yourself):
            self.graph.add_edge('D', 'D')

    def test_get_neighbours(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'C')
        self.assertEqual(self.graph.nodes['A'], set(['B', 'C']))
        self.assertEqual(self.graph.nodes['B'], set(['C']))
        self.assertEqual(self.graph.nodes['C'], set())

    def test_bfs(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'C')
        self.graph.add_edge('C', 'D')
        self.graph.add_node('E')

        self.assertEqual(self.graph.bfs('A'), set(['A', 'B', 'C', 'D']))
        self.assertEqual(self.graph.bfs('E'), set(['E']))
        self.assertEqual(self.graph.bfs('B'), set(['B', 'C', 'D']))
        self.assertEqual(self.graph.bfs('C'), set(['D', 'C']))
        self.assertEqual(self.graph.bfs('D'), set(['D']))

    def test_path_between(self):
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('A', 'C')
        self.graph.add_edge('B', 'C')
        self.graph.add_edge('C', 'D')
        self.graph.add_node('E')
        self.assertFalse(self.graph.path_between('B', 'A'))
        self.assertTrue(self.graph.path_between('A', 'D'))
        self.assertTrue(self.graph.path_between('A', 'C'))


if __name__ == '__main__':
    unittest.main()
