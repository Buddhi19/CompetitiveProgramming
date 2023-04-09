# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
 
"""This class represents a directed graph """
# using adjacency list representation
 
 
class Graph:
 
    # Constructor
    def __init__(self,vertices):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.V=vertices
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Driver code
 
if __name__=="__main__":

    V,E=map(int,input().split()) ## Take Vertices and Edges but we dont use number of vertices 

    graph=Graph(V)
 
    for _ in range(E):
        x,y=map(int,input().split())  ## take edges
        graph.addEdge(x,y)

    starting_node=int(input())

    graph.BFS(starting_node)


# Create a graph given in
# the above diagram
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
 