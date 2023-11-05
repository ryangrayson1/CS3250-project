import unittest
from utils import Graph, SiteManager

class MaxFlowCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.site_manager = SiteManager("https://visualgo.net/en/maxflow")
        self.site_manager.close_instructions()

    def test_invalid_source(self):
        graph = Graph()
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 5)

        try:
            self.site_manager.run_dinics(str(graph), 5, 0)
            # expect an exception here - should not get to a result
            self.fail()
        except:
            pass

        err = self.site_manager.get_dinics_error()
        self.assertEqual("The source vertex does not exist in the graph.", err)

    def test_invalid_sink(self):
        graph = Graph()
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 5)

        try:
            self.site_manager.run_dinics(str(graph), 0, 5)
            # expect an exception here - should not get to a result
            self.fail()
        except:
            pass

        err = self.site_manager.get_dinics_error()
        self.assertEqual("The sink vertex does not exist in the graph.", err)

    def test_calculate_max_flow_simple(self):
        graph = Graph()
        graph.add_edge(0, 2, 5)
        graph.add_edge(0, 3, 4)
        graph.add_edge(1, 4, 99)
        graph.add_edge(2, 3, 2)
        graph.add_edge(2, 1, 3)
        graph.add_edge(2, 4, 99)
        graph.add_edge(3, 1, 6)

        max_flow = self.site_manager.run_dinics(str(graph), 0, 4)

        self.assertEqual(max_flow, 9)

if __name__ == "__main__":
    unittest.main()
