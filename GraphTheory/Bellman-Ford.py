"""
detect negative cycles
"""
class MyGraph:
    def __init__(self,nodes):
        self.nodes=nodes
        self.graph=[]
        self.distance=[]
        pass

    def addEdges(self,start,end,weight):
        self.graph.append([start,end,weight])
        self.graph.append([end,start,weight]) #non directed


    def bellman_ford(self,start):
        dist=[float("Inf")]*self.nodes
        dist[start]=0

        for _ in range(self.nodes-1):
            for s,e,w in self.graph:
                if dist[s]!=float("Inf") and dist[s]+w<dist[e]:
                    dist[e]=dist[s]+w
        self.distance=dist

        for s,e,w in self.graph:
            if dist[s]!=float("Inf") and dist[s]+w<dist[e]:
                return True
        return False


def main():
    g = MyGraph(5)
    g.addEdges(0, 1, 5)
    g.addEdges(0, 2, 4)
    g.addEdges(1, 3, 3)
    g.addEdges(2, 1, 6)
    g.addEdges(3, 2, 2)

    g.bellman_ford(2)
    print(g.distance)
    for i in range(4):
        print(g.bellman_ford(i))

if __name__=="__main__":
    main()

