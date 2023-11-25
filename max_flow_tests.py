import time
import unittest
from utils import Graph, SiteManager


class MaxFlowCalculatorTests(unittest.TestCase):
    def setUp(self):
        self.site_manager = SiteManager("https://visualgo.net/en/maxflow")
        self.site_manager.close_instructions()

    # Test Case #1: A1, B1, C1, D1
    # Input Space Partition: Ford-Fulkerson, well-formed input, 0-2 nodes, connected graph
    # Description:
    # @unittest.skip("x")
    def test_ff_wellformed_2nodes_connected(self):
        graph = Graph(2)
        graph.add_edge(0, 1, 5)

        max_flow = self.site_manager.run_ford_fulkerson(str(graph), 0, 1)

        self.assertEqual(max_flow, 5)

    # Test Case #2: A1, B1, C1, D2
    # Input Space Partition: Ford-Fulkerson, well-formed input, 0-2 nodes, disconnected graph
    # Description:
    # @unittest.skip("x")
    def test_ff_wellformed_2nodes_disconnected(self):
        graph = Graph(2)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph))

        draw_msg = self.site_manager.get_draw_error()
        self.assertTrue("Source and sink is not connected." in draw_msg)

        try:
            # algo should not run with this input, err should have been displayed
            self.site_manager.ford_fulkerson(0, 1)
            self.fail()
        except:
            pass

    # Test Case #3: A1, B1, C2, D1
    # Input Space Partition: Ford-Fulkerson, well-formed input, 3-4 nodes, connected graph
    # Description:
    # @unittest.skip("x")
    def test_ff_wellformed_4nodes_connected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 7)
        graph.add_edge(2, 3, 7)

        max_flow = self.site_manager.run_ford_fulkerson(str(graph), 0, 3)

        self.assertEqual(max_flow, 7)

    # Test Case #4: A1, B1, C2, D2
    # Input Space Partition: Ford-Fulkerson, well-formed input, 3-4 nodes, disconnected graph
    # Description:
    # result: NOTE this sometimes displays the wrong error message! bug found by this test case
    # @unittest.skip("x")
    def test_ff_wellformed_4nodes_disconnected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 7)
        graph.add_edge(2, 3, 7)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph))

        draw_msg = self.site_manager.get_draw_error()
        self.assertTrue("Source and sink is not connected." in draw_msg)

        try:
            self.site_manager.run_ford_fulkerson(str(graph), 0, 4)
            self.fail()
        except:
            pass

    # Test Case #5: A1, B1, C3, D1
    # Input Space Partition: Ford-Fulkerson, well-formed input, 5-7 nodes, connected graph
    # Description:
    # @unittest.skip("x")
    def test_ff_wellformed_5nodes_connected(self):
        graph = Graph(5)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 2)
        graph.add_edge(3, 4, 4)

        max_flow = self.site_manager.run_ford_fulkerson(str(graph), 0, 4)

        self.assertEqual(max_flow, 1)

    # Test Case #6: A1, B1, C3, D2
    # Input Space Partition: Ford-Fulkerson, well-formed input, 5-7 nodes, disconnected graph
    # Description:

    # Test Case #7: A1, B1, C4, D1
    # Input Space Partition: Ford-Fulkerson, well-formed input, 8+ nodes, connected graph
    # Description:
    #  invalid sink

    # Test Case #8: A1, B1, C4, D2
    # Input Space Partition: Ford-Fulkerson, well-formed input, 8+ nodes, disconnected graph
    # Description:

    # Test Case #9: A1, B2, C1, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 0-2 nodes, connected graph
    # Description:

    # Test Case #10: A1, B2, C1, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 0-2 nodes, disconnected graph
    # Description:

    # Test Case #11: A1, B2, C2, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 3-4 nodes, connected graph
    # Description:

    # Test Case #12: A1, B2, C2, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 3-4 nodes, disconnected graph
    # Description:

    # Test Case #13: A1, B2, C3, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 5-7 nodes, connected graph
    # Description:

    # Test Case #14: A1, B2, C3, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 5-7 nodes, disconnected graph
    # Description:

    # Test Case #15: A1, B2, C4, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 8+ nodes, connected graph
    # Description:

    # Test Case #16: A1, B2, C4, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 8+ nodes, disconnected graph
    # Description:

    # Test Case #17: A2, B1, C1, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 0-2 nodes, connected graph
    # Description:

    # Test Case #18: A2, B1, C1, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 0-2 nodes, disconnected graph
    # Description:

    # Test Case #19: A2, B1, C2, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 3-4 nodes, connected graph
    # Description:

    # Test Case #20: A2, B1, C2, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 3-4 nodes, disconnected graph
    # Description:

    # Test Case #21: A2, B1, C3, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 5-7 nodes, connected graph
    # Description:

    # Test Case #22: A2, B1, C3, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 5-7 nodes, disconnected graph
    # Description:

    # Test Case #23: A2, B1, C4, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 8+ nodes, connected graph
    # Description:

    # Test Case #24: A2, B1, C4, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 8+ nodes, disconnected graph
    # Description:

    # Test Case #25: A2, B2, C1, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 0-2 nodes, connected graph
    # Description:

    # Test Case #26: A2, B2, C1, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 0-2 nodes, disconnected graph
    # Description:

    # Test Case #27: A2, B2, C2, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 3-4 nodes, connected graph
    # Description:

    # Test Case #28: A2, B2, C2, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 3-4 nodes, disconnected graph
    # Description:

    # Test Case #29: A2, B2, C3, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 5-7 nodes, connected graph
    # Description:

    # Test Case #30: A2, B2, C3, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 5-7 nodes, disconnected graph
    # Description:

    # Test Case #31: A2, B2, C4, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 8+ nodes, connected graph
    # Description:

    # Test Case #32: A2, B2, C4, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 8+ nodes, disconnected graph
    # Description:

    # Test Case #33: A3, B1, C1, D1
    # Input Space Partition: Dinic's, well-formed input, 0-2 nodes, connected graph
    # Description:

    # Test Case #34: A3, B1, C1, D2
    # Input Space Partition: Dinic’s, well-formed input, 0-2 nodes, disconnected graph
    # Description:

    # Test Case #35: A3, B1, C2, D1
    # Input Space Partition: Dinic's, well-formed input, 3-4 nodes, connected graph
    # Description:

    # Test Case #36: A3, B1, C2, D2
    # Input Space Partition: Dinic's, well-formed input, 3-4 nodes, disconnected graph
    # Description:

    # Test Case #37: A3, B1, C3, D1
    # Input Space Partition: Dinic’s, well-formed input, 5-7 nodes, connected graph
    # Description:

    # Test Case #38: A3, B1, C3, D2
    # Input Space Partition: Dinic's, well-formed input, 5-7 nodes, disconnected graph
    # Description:

    # Test Case #39: A3, B1, C4, D1
    # Input Space Partition: Dinic's, well-formed input, 8+ nodes, connected graph
    # Description:

    # Test Case #40: A3, B1, C4, D2
    # Input Space Partition: Dinic’s, well-formed input, 8+ nodes, disconnected graph
    # Description:

    # Test Case #41: A3, B2, C1, D1
    # Input Space Partition: Dinic's, malformed input, 0-2 nodes, connected graph
    # Description:

    # Test Case #42: A3, B2, C1, D2
    # Input Space Partition: Dinic's, malformed input, 0-2 nodes, disconnected graph
    # Description:

    # Test Case #43: A3, B2, C2, D1
    # Input Space Partition: Dinic’s, malformed input, 3-4 nodes, connected graph
    # Description:

    # Test Case #44: A3, B2, C2, D2
    # Input Space Partition: Dinic's, malformed input, 3-4 nodes, disconnected graph
    # Description:

    # Test Case #45: A3, B2, C3, D1
    # Input Space Partition: Dinic's, malformed input, 5-7 nodes, connected graph
    # Description:
    # @unittest.skip("x")
    def test_dinic_malformed_5nodes_connected(self):
        graph = Graph(5)
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 5)

        try:
            self.site_manager.run_dinics(str(graph), 0, 5)
            # expect an exception here - should not get to a result
            self.fail()
        except:
            err = self.site_manager.get_dinics_error()
            self.assertEqual("The sink vertex does not exist in the graph.", err)

    # Test Case #46: A3, B2, C3, D2
    # Input Space Partition: Dinic’s, malformed input, 5-7 nodes, disconnected graph
    # Description:

    # Test Case #47: A3, B2, C4, D1
    # Input Space Partition: Dinic's, malformed input, 8+ nodes, connected graph
    # Description:
    # @unittest.skip("x")
    def test_ek_malformed_10nodes_connected(self):
        graph = Graph(10)
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 5)
        graph.add_edge(4, 5, 1)
        graph.add_edge(5, 6, 2)
        graph.add_edge(6, 7, 3)
        graph.add_edge(9, 1, 4)
        graph.add_edge(1, 9, 4)
        graph.add_edge(2, 8, 5)

        try:
            self.site_manager.run_dinics(str(graph), 10, 0)
            # expect an exception here - should not get to a result
            self.fail()
        except:
            time.sleep(1)
            err = self.site_manager.get_dinics_error()
            self.assertEqual("The source vertex does not exist in the graph.", err)

    # Test Case #48: A3, B2, C4, D2
    # Input Space Partition: Dinic's, malformed input, 8+ nodes, disconnected graph
    # Description:


if __name__ == "__main__":
    unittest.main()
