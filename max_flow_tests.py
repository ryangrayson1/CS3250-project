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
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_wellformed_2nodes_connected(self):
        graph = Graph(2)
        graph.add_edge(0, 1, 5)

        max_flow = self.site_manager.run_ford_fulkerson(str(graph), 0, 1)

        self.assertEqual(max_flow, 5)

    # Test Case #2: A1, B1, C1, D2
    # Input Space Partition: Ford-Fulkerson, well-formed input, 0-2 nodes, disconnected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_wellformed_2nodes_disconnected(self):
        graph = Graph(2)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph))

        draw_msg = self.site_manager.get_draw_error()
        self.assertTrue("Source and sink is not connected" in draw_msg)

        try:
            # algo should not run with this input, err should have been displayed
            self.site_manager.ford_fulkerson(0, 1)
            self.fail()
        except:
            pass

    # Test Case #3: A1, B1, C2, D1
    # Input Space Partition: Ford-Fulkerson, well-formed input, 3-4 nodes, connected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
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
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_wellformed_4nodes_disconnected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 7)
        graph.add_edge(2, 3, 7)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph))

        draw_msg = self.site_manager.get_draw_error()
        self.assertTrue("Source and sink is not connected" in draw_msg)

        try:
            self.site_manager.run_ford_fulkerson(str(graph), 0, 4)
            self.fail()
        except:
            pass

    # Test Case #5: A1, B1, C3, D1
    # Input Space Partition: Ford-Fulkerson, well-formed input, 5-7 nodes, connected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
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
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_wellformed_6nodes_disconnected(self):
        graph = Graph(6)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 1)
        graph.add_edge(2, 3, 2)
        graph.add_edge(3, 4, 4)
        graph.add_edge(5, 0, 1)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph))

        draw_msg = self.site_manager.get_draw_error()
        self.assertTrue("Source and sink is not connected" in draw_msg)

        try:
            self.site_manager.run_ford_fulkerson(str(graph), 0, 5)
            self.fail()
        except:
            pass

    # Test Case #7: A1, B1, C4, D1
    # Input Space Partition: Ford-Fulkerson, well-formed input, 8+ nodes, connected graph
    # Description: In this test, we ensure that in 2 different spots there are multiple augmenting path options
    # this ensure we hit one of the tricky nuances of the max flow algorithm
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_wellformed_10nodes_connected(self):
        graph = Graph(10)
        graph.add_edge(0, 1, 15)
        graph.add_edge(1, 2, 25)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 5)
        graph.add_edge(4, 9, 5)
        graph.add_edge(2, 6, 7)
        graph.add_edge(4, 0, 1)
        graph.add_edge(4, 5, 31)
        graph.add_edge(5, 6, 12)
        graph.add_edge(6, 7, 53)
        graph.add_edge(7, 8, 14)
        graph.add_edge(8, 9, 5)
        graph.add_edge(9, 0, 5)
        graph.add_edge(0, 9, 5)

        max_flow = self.site_manager.run_ford_fulkerson(str(graph), 0, 9)

        self.assertEqual(max_flow, 15)

    # Test Case #8: A1, B1, C4, D2
    # Input Space Partition: Ford-Fulkerson, well-formed input, 8+ nodes, disconnected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_wellformed_20nodes_disconnected(self):
        graph = Graph(20)
        graph.add_edge(0, 1, 15)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph))

        draw_msg = self.site_manager.get_draw_error()
        self.assertTrue("Source and sink is not connected" in draw_msg)

        try:
            self.site_manager.run_ford_fulkerson(str(graph), 0, 5)
            self.fail()
        except:
            pass

    # Test Case #9: A1, B2, C1, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 0-2 nodes, connected graph
    # Description: Test an invalid edge being put in the graph input
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_malformed_2nodes_connected(self):
        graph = Graph(2)
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 2, 6)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)

        err = self.site_manager.get_input_error()
        self.assertTrue("Invalid v in line 3" in err)

        try:
            self.site_manager.run_ford_fulkerson(str(graph), 0, 1)
            self.fail()
        except:
            pass

    # Test Case #10: A1, B2, C1, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 0-2 nodes, disconnected graph
    # Description: test a self edge with an invalid string weight being put into the graph
    # Author: Ryan
    @unittest.skip("x")
    def test_ff_malformed_2nodes_disconnected(self):
        graph = Graph(2)
        graph.add_edge(0, 0, "invalid")

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)

        err = self.site_manager.get_input_error()
        self.assertTrue("Error trying to read line 2" in err)

        try:
            self.site_manager.run_ford_fulkerson(str(graph), 0, 1)
            self.fail()
        except:
            pass

    # Test Case #11: A1, B2, C2, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 3-4 nodes, connected graph
    # Description: test an invalid string input with 4 nodes, connected
    # Author: Mike
    @unittest.skip("x")
    def test_ff_malformed_4nodes_connected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, "invalid")  # invalid weight
        graph.add_edge(1, 2, 7)
        graph.add_edge(2, 3, 7)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)
        err = self.site_manager.get_input_error()
        self.assertTrue("Error trying to read line 2" in err)
        try:
            self.site_manager.run_ford_fulkerson(str(graph), 0, 3)
            self.fail()
        except:
            pass

    # Test Case #12: A1, B2, C2, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 3-4 nodes, disconnected graph
    # Description: test an invalid string input on a disconnected graph with 4 nodes
    # Author: Mike
    @unittest.skip("x")
    def test_ff_malformed_4nodes_disconnected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, "Invalid")  # invalid weight
        graph.add_edge(3, 4, 7)

        self.site_manager.open_graph_input(True)
        
        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_ford_fulkerson(str(graph), 0, 4)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 2" in err)
            pass

    # Test Case #13: A1, B2, C3, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 5-7 nodes, connected graph
    # Description: Malformed input with 6 nodes and a disconneted graph
    # Author: Mike
    @unittest.skip("x")
    def test_ff_malformed_6nodes_connected(self):
        graph = Graph(6)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, "Invalid")
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 4, 4)
        graph.add_edge(4, 5, 6)
        
        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_ford_fulkerson(str(graph), 0, 5)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 3" in err)
            pass

    # Test Case #14: A1, B2, C3, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 5-7 nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ff_malformed_7nodes_disconnected(self):
        graph = Graph(7)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, "invalid lol")
        graph.add_edge(2, 3, 3)
        graph.add_edge(4, 5, 4)
        graph.add_edge(5, 6, 6)


        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_ford_fulkerson(str(graph), 0, 6)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 3" in err)
            pass

    # Test Case #15: A1, B2, C4, D1
    # Input Space Partition: Ford-Fulkerson, malformed input, 8+ nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ff_malformed_8nodes_connected(self):
        graph = Graph(8)
        graph.add_edge(0, 1, 5)
        graph.add_edge(1, 2, 5)
        graph.add_edge(2, 3, 5)
        graph.add_edge(3, 4, 5)
        graph.add_edge("invalid", 5, 5)
        graph.add_edge(5, 6, 5)
        graph.add_edge(6, 7, 5)
        
        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_ford_fulkerson(str(graph), 0, 7)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 6" in err)
            pass

    # Test Case #16: A1, B2, C4, D2
    # Input Space Partition: Ford-Fulkerson, malformed input, 8+ nodes, disconnected graph
    # Description:
    # Author:


    # Test Case #17: A2, B1, C1, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 0-2 nodes, connected graph
    # Description: Test an empty graph
    # Author: Ryan
    @unittest.skip("x")
    def test_ek_wellformed_0nodes_connected(self):
        graph = Graph(0)

        self.site_manager.open_graph_input(True)
        self.site_manager.set_graph(str(graph))

        draw_msg = self.site_manager.get_draw_error()
        self.assertTrue("Graph cannot be empty" in draw_msg)

        try:
            max_flow = self.site_manager.run_edmonds_karp(str(graph), 0, 0)
        except:
            pass

    # Test Case #18: A2, B1, C1, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 0-2 nodes, disconnected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
    def test_ek_wellformed_1node_disconnected(self):
        graph = Graph(1)

        # should not get a max flow result here so check the -1
        max_flow = self.site_manager.run_edmonds_karp(str(graph), 0, 0, True)

        self.assertEqual(max_flow, -1)

        err = self.site_manager.get_edmonds_karp_error()
        self.assertTrue("The source vertex is the same as the sink vertex" in err)

    # Test Case #19: A2, B1, C2, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 3-4 nodes, connected graph
    # Description: testing a classic max flow example here, one that Edmonds-Karp is able solve
    # much more quickly than Ford-Fulkerson can because Ford fulkerson will propogate back and
    # forth between the 2 augmenting paths, adding one flow unit at a time. Edmonds-Karp will
    # find the shortest augmenting path first and add all the flow units it can to that path
    # Author: Ryan
    @unittest.skip("x")
    def test_ek_wellformed_4nodes_connected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 1e8)
        graph.add_edge(0, 2, 1e8)

        graph.add_edge(1, 2, 1)

        graph.add_edge(1, 3, 1e8)
        graph.add_edge(2, 3, 1e8)

        max_flow = self.site_manager.run_edmonds_karp(str(graph), 0, 3)

        self.assertEqual(max_flow, 2e8)

    # Test Case #20: A2, B1, C2, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 3-4 nodes, disconnected graph
    # Description: Tests the case where there is a dangling node and we check the flow on a connected part of the graph
    # Result: Bug found! This test case fails because the site incorrectly detects an irrelevant error
    # Author: Ryan
    @unittest.skip("x")
    def test_ek_wellformed_3nodes_disconnected(self):
        graph = Graph(3)
        graph.add_edge(0, 2, 1e8)
        graph.add_edge(2, 0, 1e8)

        max_flow = self.site_manager.run_edmonds_karp(str(graph), 0, 2, True)

        self.assertEqual(max_flow, 1e8)

    # Test Case #21: A2, B1, C3, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 5-7 nodes, connected graph
    # Description: complete graph (all edge pairs are connected). this is useful because it tests the max flow
    # algortithm's ability to choose between many augmenting paths - an intricate part of the algorithm
    # Result: While this test case computes the correct answer, there is a bug in the UI! As you can see, the edge from
    # 0 to 4 and from 1 to 3 are hidden behind other edges. This is not a major bug but certainly an inconvenience to the
    # user
    # Author: Ryan
    @unittest.skip("x")
    def test_ek_wellformed_5nodes_connected(self):
        graph = Graph(5)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 2)
        graph.add_edge(0, 3, 3)
        graph.add_edge(0, 4, 4)
        graph.add_edge(1, 2, 5)
        graph.add_edge(1, 3, 6)
        graph.add_edge(1, 4, 7)
        graph.add_edge(2, 3, 8)
        graph.add_edge(2, 4, 9)
        graph.add_edge(3, 4, 10)

        max_flow = self.site_manager.run_edmonds_karp(str(graph), 0, 4)

        self.assertEqual(max_flow, 10)

    # Test Case #22: A2, B1, C3, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 5-7 nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_wellformed_5nodes_connected(self):
        graph = Graph(5)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 2)
        graph.add_edge(1, 2, 5)
        graph.add_edge(3, 4, 10)

        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_edmonds_karp(str(graph), 0, 4)
            self.fail()
        except:
            err = self.site_manager.get_draw_error()
            self.assertTrue("Source and sink is not connected" in err)
            pass



    # Test Case #23: A2, B1, C4, D1
    # Input Space Partition: Edmonds-Karp, well-formed input, 8+ nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_wellformed_8nodes_connected(self):
        graph = Graph(8)
        # Add edges to form a fully connected graph with valid capacities
        graph.add_edge(0, 1, 10)
        graph.add_edge(0, 2, 15)
        graph.add_edge(1, 3, 10)
        graph.add_edge(2, 4, 15)
        graph.add_edge(3, 5, 10)
        graph.add_edge(4, 5, 10)
        graph.add_edge(5, 6, 20)
        graph.add_edge(6, 7, 25)
        graph.add_edge(1, 7, 5)
        graph.add_edge(2, 6, 5)
        graph.add_edge(3, 7, 5)
        graph.add_edge(4, 7, 5)


        max_flow = self.site_manager.run_edmonds_karp(str(graph), 0, 7)
        self.assertTrue(max_flow == 25 )


    # Test Case #24: A2, B1, C4, D2
    # Input Space Partition: Edmonds-Karp, well-formed input, 8+ nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_wellformed_10nodes_connected(self):
        graph = Graph(10)
        # Add edges to form a fully connected graph with valid capacities
        graph.add_edge(0, 1, 10)
        graph.add_edge(0, 2, 15)
        graph.add_edge(1, 3, 10)
        graph.add_edge(2, 4, 15)
        graph.add_edge(5, 6, 20)
        graph.add_edge(6, 7, 25)
        graph.add_edge(7, 8, 20)
        graph.add_edge(7, 9, 17)
        graph.add_edge(8, 9, 25)
        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_edmonds_karp(str(graph), 0, 9)
            self.fail()
        except:
            err = self.site_manager.get_draw_error()
            self.assertTrue("Source and sink is not connected" in err)
            pass

    # Test Case #25: A2, B2, C1, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 0-2 nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_malformed_2nodes_connected(self):
        graph = Graph(2)
        graph.add_edge(0, 1, "invalid")

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)

        err = self.site_manager.get_input_error()
        self.assertTrue("Error trying to read line 2" in err)

        try:
            self.site_manager.run_edmonds_karp(str(graph), 0, 1)
            self.fail()
        except:
            pass

    # Test Case #26: A2, B2, C1, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 0-2 nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_malformed_2nodes_disconnected(self):
        graph = Graph(2)
        graph.add_edge(0, 0, "invalid")
        graph.add_edge(1, 1, 7)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)

        err = self.site_manager.get_input_error()
        self.assertTrue("Error trying to read line 2" in err)

        try:
            self.site_manager.run_edmonds_karp(str(graph), 0, 1)
            self.fail()
        except:
            pass

    # Test Case #27: A2, B2, C2, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 3-4 nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_malformed_4nodes_connected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, "invalid")  # invalid weight
        graph.add_edge(1, 2, 7)
        graph.add_edge(2, 3, 7)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)
        err = self.site_manager.get_input_error()
        self.assertTrue("Error trying to read line 2" in err)
        try:
            self.site_manager.run_edmonds_karp(str(graph), 0, 3)
            self.fail()
        except:
            pass

    # Test Case #28: A2, B2, C2, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 3-4 nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_malformed_4nodes_disconnected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, "Invalid")  # invalid weight
        graph.add_edge(3, 4, 7)

        self.site_manager.open_graph_input(True)
        
        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_edmonds_karp(str(graph), 0, 4)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 2" in err)
            pass

    # Test Case #29: A2, B2, C3, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 5-7 nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_malformed_6nodes_connected(self):
        graph = Graph(6)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, "Invalid")
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 4, 4)
        graph.add_edge(4, 5, 6)
        
        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_edmonds_karp(str(graph), 0, 5)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 3" in err)
            pass

    # Test Case #30: A2, B2, C3, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 5-7 nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_ek_malformed_7nodes_disconnected(self):
        graph = Graph(7)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, "invalid lol")
        graph.add_edge(2, 3, 3)
        graph.add_edge(4, 5, 4)
        graph.add_edge(5, 6, 6)


        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_edmonds_karp(str(graph), 0, 6)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 3" in err)
            pass

    # Test Case #31: A2, B2, C4, D1
    # Input Space Partition: Edmonds-Karp, malformed input, 8+ nodes, connected graph
    # Description: Here we provide input where the sink node just has an outgoing edge and is not reachable
    # Author: Ryan
    @unittest.skip("x")
    def test_ek_malformed_10nodes_connected(self):
        graph = Graph(10)

        graph.add_edge(0, 2, 9)
        graph.add_edge(2, 4, 9)
        graph.add_edge(4, 6, 9)
        graph.add_edge(6, 8, 9)
        graph.add_edge(1, 3, 9)
        graph.add_edge(3, 5, 9)
        graph.add_edge(5, 7, 9)
        graph.add_edge(9, 7, 9)

        self.site_manager.open_graph_input()
        self.site_manager.set_graph(str(graph), False)

        msg = self.site_manager.get_input_error()

        self.assertTrue("graph must be connected for flows" in msg)

    # Test Case #32: A2, B2, C4, D2
    # Input Space Partition: Edmonds-Karp, malformed input, 8+ nodes, disconnected graph
    # Description:
    # Author:

    # Test Case #33: A3, B1, C1, D1
    # Input Space Partition: Dinic's, well-formed input, 0-2 nodes, connected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
    def test_dinic_wellformed_2nodes_connected(self):
        graph = Graph(2)
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 0, 1)

        max_flow = self.site_manager.run_dinics(str(graph), 0, 1, True)

        self.assertEqual(max_flow, 1)

    # Test Case #34: A3, B1, C1, D2
    # Input Space Partition: Dinic’s, well-formed input, 0-2 nodes, disconnected graph
    # Description:
    # Author:

    # Test Case #35: A3, B1, C2, D1
    # Input Space Partition: Dinic's, well-formed input, 3-4 nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_dinic_wellformed_4nodes_connected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, 7)
        graph.add_edge(1, 2, 7)
        graph.add_edge(2, 3, 7)

        max_flow = self.site_manager.run_dinics(str(graph), 0, 3)

        self.assertEqual(max_flow, 7)


    # Test Case #36: A3, B1, C2, D2
    # Input Space Partition: Dinic's, well-formed input, 3-4 nodes, disconnected graph
    # Description:
    # Author:

    # Test Case #37: A3, B1, C3, D1
    # Input Space Partition: Dinic’s, well-formed input, 5-7 nodes, connected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
    def test_dinic_wellformed_5nodes_connected(self):
        graph = Graph(5)
        graph.add_edge(0, 2, 5)
        graph.add_edge(0, 3, 4)
        graph.add_edge(1, 4, 99)
        graph.add_edge(2, 3, 2)
        graph.add_edge(2, 1, 3)
        graph.add_edge(2, 4, 99)
        graph.add_edge(3, 1, 6)

        max_flow = self.site_manager.run_dinics(str(graph), 0, 4)

        self.assertEqual(max_flow, 9)

    # Test Case #38: A3, B1, C3, D2
    # Input Space Partition: Dinic's, well-formed input, 5-7 nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_dinic_wellformed_5nodes_connected(self):
        graph = Graph(5)
        graph.add_edge(0, 1, 1)
        graph.add_edge(0, 2, 2)
        graph.add_edge(1, 2, 5)
        graph.add_edge(3, 4, 10)

        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_dinics(str(graph), 0, 4)
            self.fail()
        except:
            err = self.site_manager.get_draw_error()
            self.assertTrue("Source and sink is not connected" in err)
            pass

    # Test Case #39: A3, B1, C4, D1
    # Input Space Partition: Dinic's, well-formed input, 8+ nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_dinic_wellformed_8nodes_connected(self):
        graph = Graph(8)
        # Add edges to form a fully connected graph with valid capacities
        graph.add_edge(0, 1, 10)
        graph.add_edge(0, 2, 15)
        graph.add_edge(1, 3, 10)
        graph.add_edge(2, 4, 15)
        graph.add_edge(3, 5, 10)
        graph.add_edge(4, 5, 10)
        graph.add_edge(5, 6, 20)
        graph.add_edge(6, 7, 25)
        graph.add_edge(1, 7, 5)
        graph.add_edge(2, 6, 5)
        graph.add_edge(3, 7, 5)
        graph.add_edge(4, 7, 5)


        max_flow = self.site_manager.run_dinics(str(graph), 0, 7)
        self.assertTrue(max_flow == 25 )

    # Test Case #40: A3, B1, C4, D2
    # Input Space Partition: Dinic’s, well-formed input, 8+ nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_dinic_wellformed_10nodes_connected(self):
        graph = Graph(10)
        # Add edges to form a fully connected graph with valid capacities
        graph.add_edge(0, 1, 10)
        graph.add_edge(0, 2, 15)
        graph.add_edge(1, 3, 10)
        graph.add_edge(2, 4, 15)
        graph.add_edge(5, 6, 20)
        graph.add_edge(6, 7, 25)
        graph.add_edge(7, 8, 20)
        graph.add_edge(7, 9, 17)
        graph.add_edge(8, 9, 25)
        self.site_manager.open_graph_input(True)

        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_dinics(str(graph), 0, 9)
            self.fail()
        except:
            err = self.site_manager.get_draw_error()
            self.assertTrue("Source and sink is not connected" in err)
            pass

    # Test Case #41: A3, B2, C1, D1
    # Input Space Partition: Dinic's, malformed input, 0-2 nodes, connected graph
    # Description:
    # Author:

    # Test Case #42: A3, B2, C1, D2
    # Input Space Partition: Dinic's, malformed input, 0-2 nodes, disconnected graph
    # Description:
    # Author:
    @unittest.skip("x")
    def test_dinic_malformed_2nodes_disconnected(self):
        graph = Graph(2)
        graph.add_edge(0, 0, "invalid")
        graph.add_edge(1, 1, 7)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)

        err = self.site_manager.get_input_error()
        self.assertTrue("Error trying to read line 2" in err)

        try:
            self.site_manager.run_dinics(str(graph), 0, 1)
            self.fail()
        except:
            pass

    # Test Case #43: A3, B2, C2, D1
    # Input Space Partition: Dinic’s, malformed input, 3-4 nodes, connected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_dinic_malformed_4nodes_connected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, "invalid")  # invalid weight
        graph.add_edge(1, 2, 7)
        graph.add_edge(2, 3, 7)

        self.site_manager.open_graph_input(True)

        self.site_manager.set_graph(str(graph), False)
        err = self.site_manager.get_input_error()
        self.assertTrue("Error trying to read line 2" in err)
        try:
            self.site_manager.run_dinics(str(graph), 0, 3)
            self.fail()
        except:
            pass

    # Test Case #44: A3, B2, C2, D2
    # Input Space Partition: Dinic's, malformed input, 3-4 nodes, disconnected graph
    # Description:
    # Author: Mike
    @unittest.skip("x")
    def test_dinic_malformed_4nodes_disconnected(self):
        graph = Graph(4)
        graph.add_edge(0, 1, "Invalid")  # invalid weight
        graph.add_edge(3, 4, 7)

        self.site_manager.open_graph_input(True)
        
        try:
            self.site_manager.set_graph(str(graph))
            self.site_manager.run_dinics(str(graph), 0, 4)
            self.fail()
        except:
            err = self.site_manager.get_input_error()
            self.assertTrue("Error trying to read line 2" in err)
            pass

    # Test Case #45: A3, B2, C3, D1
    # Input Space Partition: Dinic's, malformed input, 5-7 nodes, connected graph
    # Description: Test that a valid graph with invalid sink vertex supplied produces an appropriate error message
    # Author: Ryan
    @unittest.skip("x")
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
            self.assertTrue("The sink vertex does not exist in the graph" in err)

    # Test Case #46: A3, B2, C3, D2
    # Input Space Partition: Dinic’s, malformed input, 5-7 nodes, disconnected graph
    # Description:
    # Author:

    # Test Case #47: A3, B2, C4, D1
    # Input Space Partition: Dinic's, malformed input, 8+ nodes, connected graph
    # Description:
    # Author: Ryan
    @unittest.skip("x")
    def test_dinic_malformed_10nodes_connected(self):
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
            self.assertTrue("The source vertex does not exist in the graph" in err)

    # Test Case #48: A3, B2, C4, D2
    # Input Space Partition: Dinic's, malformed input, 8+ nodes, disconnected graph
    # Description:
    # Author:


if __name__ == "__main__":
    unittest.main()
