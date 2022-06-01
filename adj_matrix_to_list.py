class adj_matrix_to_list():
    adjacency_matrix = []
    adjacency_list = []

    def adjacency_matrix_to_adjacency_lists(self):
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix[i])):
                if self.adjacency_matrix[i][j] == 1:
                    self.adjacency_list[i].append(j)

    def print_adjacency_lists(self):
        print(self.adjacency_list)

    def add_adjacency_matrix(self, adjacency_matrix):
        self.adjacency_matrix = adjacency_matrix
        for i in range(len(adjacency_matrix)):
            self.adjacency_list.append([])


adj_matrix = adj_matrix_to_list()
adj_matrix.add_adjacency_matrix(
    [[0, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]])
adj_matrix.adjacency_matrix_to_adjacency_lists()
adj_matrix.print_adjacency_lists()
