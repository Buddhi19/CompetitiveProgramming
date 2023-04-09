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
        visited = [False] * (self.V + 1)
 
        # Create a queue for BFS
        queue = []
    
        #create a set for can visit
        set1=set()
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            set1.add(s)
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        return set1
    
    def new_roads(self):
        total_nodes={i for i in range(1,self.V+1)}
        for node in total_nodes:
            not_visited=total_nodes-self.BFS(node)
            print(f"{node}",not_visited)
 
# Driver code
 
if __name__=="__main__":

    V,E=map(int,input().split()) ## Take Vertices and Edges but we dont use number of vertices 

    graph=Graph(V)
 
    for _ in range(E):
        x,y=map(int,input().split())  ## take edges
        graph.addEdge(x,y)

    graph.new_roads()