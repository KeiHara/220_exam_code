class dfs:
    def __init__(self, v):  # v = number of vertices
        self.forward_arc_count = 0
        self.time = 0
        self.v = v
        self.e = 0
        self.graph_list = [[] for _ in range(v)]
        self.colors = ['WHITE' for _ in range(v)]
        self.seen = [[] for _ in range(v)]
        self.pred = [[] for _ in range(v)]
        self.done = [[] for _ in range(v)]
        self.tree_edges = []

    def print_graph_list(self):
        print("Adjacency List Representation:")
        for i in range(self.v):
            print(i, "-->", *self.graph_list[i])
        print()

    def add_edges(self, u, edges):
        self.graph_list[u] = (edges)
        self.e += len(edges)

    def dfs(self, selected_node):
        self.recursive_dfs_visit(selected_node)
        for node in range(self.v):
            if self.colors[node] == 'WHITE':
                self.recursive_dfs_visit(node)
        for i in range(len(self.pred)):
            if self.pred[i] or self.pred[i] == 0:
                self.tree_edges.append((self.pred[i], i))

    def recursive_dfs_visit(self, node):
        self.colors[node] = 'GRAY'
        self.seen[node] = self.time
        self.time += 1
        for neighbour in self.graph_list[node]:
            if self.colors[neighbour] == 'WHITE':
                self.pred[neighbour] = node
                self.recursive_dfs_visit(neighbour)
        self.colors[node] = 'BLACK'
        self.done[node] = self.time
        self.time += 1

    def print_tree_edges(self):
        print(self.tree_edges)

    def print_done_time(self):
        print(self.done)

    def print_seen_time(self):
        print(self.seen)

    def print_pred(self):
        print(self.pred)

    def check_forward_cross_arc(self):
        for node in range(self.v):
            for neighbour in self.graph_list[node]:
                if (node, neighbour) not in self.tree_edges and self.seen[node] < self.seen[neighbour] < self.done[neighbour] < self.done[node]:
                    self.forward_arc_count += 1
                elif (node, neighbour) not in self.tree_edges and self.seen[neighbour] < self.done[neighbour] < self.seen[node] < self.done[node]:
                    self.forward_arc_count += 1
        return self.forward_arc_count


def check_ancestor(seen, done, v, w):
    if (seen[v] < seen[w] and done[v] > done[w]):
        return "Tree or forward edge"
    elif (seen[v] > seen[w] and done[v] < done[w]):
        return "Back edge"
    elif (seen[v] > seen[w] and done[v] > done[w]):
        return "Cross edge"


graph = dfs(6)
graph.add_edges(0, [3, 5])  # 0 --> 1, 2, 3 eg
graph.add_edges(1, [2])
graph.add_edges(2, [])
graph.add_edges(3, [4])
graph.add_edges(4, [])
graph.add_edges(5, [4])
graph.dfs(4)
graph.print_pred()


print(check_ancestor([0, 1, 3, 6, 5], [9, 2, 4, 7, 8], 3, 1))
