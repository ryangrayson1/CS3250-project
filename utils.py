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


WAIT = .5
# do and wait for page load
def dw(fn):
    fn()
    time.sleep(WAIT)

class SiteManager:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def close_instructions(self):
        overlay = self.driver.find_element(By.ID, "overlay")
        dw(overlay.click)

    def open_graph_input(self):
        edit_graph_button = self.driver.find_element(By.ID, "draw")
        dw(edit_graph_button.click)
        graph_input_button = self.driver.find_element(By.ID, "graph-input")
        dw(graph_input_button.click)
        # set to 0-indexed
        graph_type = self.driver.find_element(By.NAME, "indexing-option")
        graph_type.find_element(By.XPATH, "//input[@value='0-Index']").click()
        # set the type to flow
        graph_type = self.driver.find_element(By.NAME, "graph-drawing-type")
        dw(graph_type.find_element(By.XPATH, "//input[@value='Flow']").click)

    # assumes graph input field is already open
    def set_graph(self, graph_str):
        # set the text in the graph input field
        graph_spec = self.driver.find_element(By.ID, "graph-input-field")
        graph_spec.clear()
        graph_spec.send_keys(graph_str)
        # submit this graph
        graph_options = self.driver.find_element(By.ID, "graph-input-options")
        submit_button = graph_options.find_element(By.XPATH, "//button[contains(@onclick, 'create_graph(true)')]")
        dw(submit_button.click)
        done_button = self.driver.find_element(By.CLASS_NAME, "done-button")
        dw(done_button.click)

    def dinics(self, s, t):
        dinic = self.driver.find_element(By.ID, "dinic")
        dw(dinic.click)
        source = self.driver.find_element(By.ID, "dinic-sourcevertex")
        source.clear()
        source.send_keys(s)
        sink = self.driver.find_element(By.ID, "dinic-sinkvertex")
        sink.clear()
        sink.send_keys(t)
        go = self.driver.find_element(By.ID, "dinic-go")
        dw(go.click)
        finish = self.driver.find_element(By.ID, "go-to-end")
        dw(finish.click)
        result = self.driver.find_element(By.ID, "status").text
        max_flow = result.split(".")[0][-1]
        return int(max_flow)

    def run_dinics(self, graph_str, s, t):
        self.open_graph_input()
        self.set_graph(graph_str)
        return self.dinics(s, t)

    def get_dinics_error(self):
        return self.driver.find_element(By.ID, "dinic-err").text

    def __del__(self):
        self.driver.close()
        self.driver.quit()
