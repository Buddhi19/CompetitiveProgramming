#consider a graph of 5 nodes
# graph=[[2,3],[4,3],[0,4],[0,1],[1,2]]
# I will implement a code to backtrack the nodes

n=5
graph=[[2,3],[4,3],[0,4],[0,1],[1,2]]

visited=[False for i in range(n)]

def backtrackdfs(node):
    if visited[node]==True:
        return
    visited[node]=True

    neighbours=graph[node]
    for next in neighbours:
        backtrackdfs(next)
    
backtrackdfs(0)
print(visited)