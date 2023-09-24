
from collections import defaultdict

class BFS:
  def __init__(self,n) -> None:
    self.n=n
    self.graph=defaultdict(list)
    self.visited=[False for i in range(n)]

  def addEdge(self,start,end):
    self.graph[start].append(end)

  def bfs(self,start):
    self.visited[start]=True
    
    queue=[]
    queue.append(start)

    while queue:
      s=queue.pop(0)
      for node in self.graph[s]:
        if self.visited[node]==False:
          queue.append(node)
          self.visited[node]=True


if __name__=="__main__":
  g=BFS(4)
  g.addEdge(0, 1)
  g.addEdge(0, 2)
  g.addEdge(1, 2)
  g.addEdge(2, 0)
  g.addEdge(2, 3)
  g.addEdge(3, 3)

  g.bfs(1)
  print(g.visited)

