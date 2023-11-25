import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_edge(self, u, v, w):
        self.nodes.add(u)
        self.nodes.add(v)
        self.edges.append((u, v, w))

    def __str__(self):
        s = f"{max(self.nodes) + 1} {len(self.edges)}\n"
        for u, v, w in self.edges:
            s += f"{u} {v} {w}\n"
        return s


WAIT = 0.5


# click and wait for page load
def cw(elem):
    elem.click()
    time.sleep(WAIT)


class SiteManager:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def close_instructions(self):
        overlay = self.driver.find_element(By.ID, "overlay")
        cw(overlay)

    def open_graph_input(self):
        edit_graph_button = self.driver.find_element(By.ID, "draw")
        cw(edit_graph_button)
        graph_input_button = self.driver.find_element(By.ID, "graph-input")
        cw(graph_input_button)
        # set to 0-indexed
        graph_type = self.driver.find_element(By.NAME, "indexing-option")
        graph_type.find_element(By.XPATH, "//input[@value='0-Index']").click()
        # set the type to flow
        graph_type = self.driver.find_element(By.NAME, "graph-drawing-type")
        cw(graph_type.find_element(By.XPATH, "//input[@value='Flow']"))

    # assumes graph input field is already open
    def set_graph(self, graph_str):
        # set the text in the graph input field
        graph_spec = self.driver.find_element(By.ID, "graph-input-field")
        graph_spec.clear()
        graph_spec.send_keys(graph_str)
        # submit this graph
        graph_options = self.driver.find_element(By.ID, "graph-input-options")
        submit_button = graph_options.find_element(
            By.XPATH, "//button[contains(@onclick, 'create_graph(true)')]"
        )
        cw(submit_button)
        done_button = self.driver.find_element(By.CLASS_NAME, "done-button")
        cw(done_button)

    def ford_fulkerson(self, s, t):
        ff = self.driver.find_element(By.ID, "fordfulkerson")
        cw(ff)
        source = self.driver.find_element(By.ID, "fordfulkerson-sourcevertex")
        source.clear()
        source.send_keys(s)
        sink = self.driver.find_element(By.ID, "fordfulkerson-sinkvertex")
        sink.clear()
        sink.send_keys(t)
        go = self.driver.find_element(By.ID, "fordfulkerson-go")
        cw(go)
        finish = self.driver.find_element(By.ID, "go-to-end")
        cw(finish)
        result = self.driver.find_element(By.ID, "status").text
        max_flow = result.split(".")[0][-1]
        return int(max_flow)

    def dinics(self, s, t):
        dinic = self.driver.find_element(By.ID, "dinic")
        cw(dinic)
        source = self.driver.find_element(By.ID, "dinic-sourcevertex")
        source.clear()
        source.send_keys(s)
        sink = self.driver.find_element(By.ID, "dinic-sinkvertex")
        sink.clear()
        sink.send_keys(t)
        go = self.driver.find_element(By.ID, "dinic-go")
        cw(go)
        finish = self.driver.find_element(By.ID, "go-to-end")
        cw(finish)
        result = self.driver.find_element(By.ID, "status").text
        max_flow = result.split(".")[0][-1]
        return int(max_flow)

    def run_ford_fulkerson(self, graph_str, s, t):
        self.open_graph_input()
        self.set_graph(graph_str)
        return self.ford_fulkerson(s, t)

    def get_ford_fulkerson_error(self):
        return self.driver.find_element(By.ID, "fordfulkerson-err").text

    def run_edmonds_karp(self, graph_str, s, t):
        self.open_graph_input()
        self.set_graph(graph_str)
        return self.edmonds_karp(s, t)

    def run_dinics(self, graph_str, s, t):
        self.open_graph_input()
        self.set_graph(graph_str)
        return self.dinics(s, t)

    def get_dinics_error(self):
        return self.driver.find_element(By.ID, "dinic-err").text

    def __del__(self):
        self.driver.close()
        self.driver.quit()
