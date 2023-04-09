from collections import defaultdict
 
"""This class represents a directed graph """
# using adjacency list representation
 
 
class Graph:
 
    # Constructor
    def __init__(self,vertices):
        self.V=vertices
        self.graph={x:set() for x in range(1,self.V+1)}
        # print(self.graph)

    def addEdge(self,x,y):
        self.graph[x].add(y)  ## for directed graph
        # self.graph[y].add(x)  ## for undirected graph
        
    def shortest_path(self, node1, node2):
        path_list = [[node1]]
        path_index = 0
        # To keep track of previously visited nodes
        previous_nodes = {node1}
        if node1 == node2:
            return path_list[0]
            
        while path_index < len(path_list):
            current_path = path_list[path_index]
            last_node = current_path[-1]
            next_nodes = self.graph[last_node]
            # Search goal node
            if node2 in next_nodes:
                current_path.append(node2)
                return current_path
            # Add new paths
            for next_node in next_nodes:
                if not next_node in previous_nodes:
                    new_path = current_path[:]
                    new_path.append(next_node)
                    path_list.append(new_path)
                    # To avoid backtracking
                    previous_nodes.add(next_node)
            # Continue to next path in list
            path_index += 1
        # No path is found
        return [-1]


 
if __name__=="__main__":

    V,E=map(int,input().split()) ## Take Vertices and Edges but we dont use number of vertices 

    graph=Graph(V)
 
    for _ in range(E):
        x,y=map(int,input().split())  ## take edges
        graph.addEdge(x,y)
    start=int(input())
    end=int(input())
    print(*graph.shortest_path(start,end))