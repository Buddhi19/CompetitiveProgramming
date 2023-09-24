class MyGraph:
    def __init__(self,nodes):
        self.graph=[[0 for i in range(nodes)] for j in range(nodes)]
        pass

    def add_edge(self,start,end,weight):
        self.graph[start][end]=weight

    def print_matrix(self):
        for row in self.graph:
            for val in row:
                print(val,end=' ')
            print()

def main():
    g = MyGraph(5)
    g.add_edge(0, 1,1)
    g.add_edge(0, 2,1)
    g.add_edge(1, 2,1)
    g.add_edge(2, 0,1)
    g.add_edge(2, 3,1)

    g.print_matrix()


if __name__ == '__main__':
    main()