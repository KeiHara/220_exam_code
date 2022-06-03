class bfs:
    def __init__(self, v):
        self.v = v
        self.e = 0
        self.queue = []
        self.colors = ['WHITE' for _ in range(v)]
        self.graph_list = [[] for _ in range(v)]
        self.pred = [[] for _ in range(v)]
        self.seen = [[] for _ in range(v)]
        self.done = [[] for _ in range(v)]
        self.tree_edges = []
        self.time = 0

    def print_graph_list(self):
        print("Adjacency List Representation:")
        for i in range(self.v):
            print(i, "-->", *self.graph_list[i])
        print()

    def add_edges(self, u, edges):
        self.graph_list[u] = (edges)
        self.e += len(edges)

    def bfs(self, selected_node):
        self.bfs_visit(selected_node)
        for node in range(self.v):
            if self.colors[node] == 'WHITE':
                self.bfs_visit(node)
        for i in range(len(self.pred)):
            if self.pred[i] or self.pred[i] == 0:
                self.tree_edges.append((self.pred[i], i))

    def bfs_visit(self, node):
        self.colors[node] = 'GRAY'
        self.seen[node] = self.time
        self.time += 1
        self.queue.append(node)
        while self.queue:
            node = self.queue.pop(0)
            for neighbour in self.graph_list[node]:
                if self.colors[neighbour] == 'WHITE':
                    self.pred[neighbour] = node
                    self.colors[neighbour] = 'GRAY'
                    self.seen[neighbour] = self.time
                    self.time += 1
                    self.queue.append(neighbour)
        self.colors[node] = 'BLACK'
        self.done[node] = self.time
        self.time += 1

    def print_tree_edges(self):
        print(self.tree_edges)

    def print_pred(self):
        print(self.pred)

    def print_done_time(self):
        print(self.done)

    def print_seen_time(self):
        print(self.seen)


graph = bfs(7)
graph.add_edges(1, [])
graph.add_edges(2, [1])
graph.add_edges(3, [1])
graph.add_edges(4, [1, 2])
graph.add_edges(5, [2, 4, 7])
graph.add_edges(6, [4, 5, 7])
graph.add_edges(7, [3])
graph.bfs(4)
graph.print()
