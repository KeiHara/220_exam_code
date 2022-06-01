class adj_list_to_matrix:
    adjacency_matrix = []
    adjacency_list = []

    def adjacency_lists_to_adjacency_matrices(self):
        for i in range(len(self.adjacency_list)):
            for index in self.adjacency_list[i]:
                self.adjacency_matrix[i][index] = 1

    def print_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            print(row)

    def add_adjacency_list(self, adjacency_list):
        self.adjacency_list = adjacency_list
        for i in range(len(adjacency_list)):
            self.adjacency_matrix.append([])
            for j in range(len(adjacency_list)):
                self.adjacency_matrix[i].append(0)


adj_list = adj_list_to_matrix()
# 0 --> 1, 3, 5
# 1 --> 0
# 2 --> 0, 5
# 3 --> 2
# 4 --> 5
# 5 --> none
adj_list.add_adjacency_list([[1, 3, 5], [0], [0, 5], [2], [5], []])
adj_list.adjacency_lists_to_adjacency_matrices()
adj_list.print_adjacency_matrix()
