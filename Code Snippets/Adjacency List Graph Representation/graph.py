"""
A Python program to demonstrate the adjacency
list representation of the graph
"""
 
# A class to represent the adjacency list of the node
 
 
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
 
 
# A class to represent a graph. A graph
# is the list of the adjacency lists.
# Size of the array will be the no. of the
# vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
 
    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
 
    # Function to print the graph
    def print_graph(self):
        matrix=[[] for i in range(self.V)]
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                matrix[i].append(temp.vertex)
                temp = temp.next
        print(matrix)
 
# Driver program to the above graph class
if __name__ == "__main__":
    V,t = map(int,input().split())   # Takes number of Vertices-> V and number of Edges->t
    graph = Graph(V)

    for _ in range(t):
        x,y=map(int,input().split())
        graph.add_edge(x,y)
    
    graph.print_graph()