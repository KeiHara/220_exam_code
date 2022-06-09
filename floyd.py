INF = 999


class floyd:
    nV = 0
    g = []

    def __init__(self, g):
        self.g = g
        self.nV = len(g)

    # Algorithm implementation
    def floyd_warshall(self):
        distance = list(map(lambda i: list(map(lambda j: j, i)), self.g))

        # Adding vertices individually
        for k in range(self.nV):
            self.print_solution(distance)
            print()
            for i in range(self.nV):
                for j in range(self.nV):
                    distance[i][j] = min(
                        distance[i][j], distance[i][k] + distance[k][j])
        self.print_solution(distance)

    # Printing the solution

    def print_solution(self, distance):
        for i in range(self.nV):
            for j in range(self.nV):
                if(distance[i][j] == INF):
                    print("INF", end=" ")
                else:
                    print(distance[i][j], end="  ")
            print(" ")


G = [[0, 3, INF, 3, 1],
     [4, 0, 2, INF, INF],
     [INF, INF, 0, INF, 1],
     [INF, INF, INF, 0, INF],
     [INF, 1, INF, 1, 0]
     ]

ans = floyd(G)
ans.floyd_warshall()
