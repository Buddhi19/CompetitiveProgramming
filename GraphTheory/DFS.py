
class DFS:
    def __init__(self,n) -> None:
        self.n=n
        self.graph=[[] for i in range(n)]
        self.visited=[False for i in range(n)]

    def graph_update(self,start,end):
        """
        not a directed graph
        """
        self.graph[start-1].append(end-1)
        self.graph[end-1].append(start-1)

    def dfs(self,s):
        if self.visited[s]==True:
            return
        self.visited[s]=True

        for node in self.graph[s]:
            self.dfs(node)


mygraph=DFS(5)
mygraph.graph_update(1,2)
mygraph.graph_update(1,5)
mygraph.graph_update(5,2)
mygraph.graph_update(2,3)
mygraph.graph_update(5,3)

mygraph.dfs(0)

print(mygraph.visited)

