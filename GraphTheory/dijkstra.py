from queue import PriorityQueue

def dijkstra(G, start, end):
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()
  
    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get() 
            if vertex not in visited: break
        else:
            break 
        visited.add(vertex)
        if vertex == end:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue
            old_cost = cost.get(neighbor, float('inf'))
            new_cost = cost[vertex] + distance
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return parent

def path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1]


def main():
    N,M=map(int,input().split())
    Graph={}
    for i in range(1,N+1):
        Graph[i]=set()

    for i in range(M):
        u,v,w=map(int,input().split())
        Graph[u].add((v,w))
        Graph[v].add((u,w))

    start,end=map(int,input().split())

    parent=dijkstra(Graph,start,end)
    print(path(parent,end))


if __name__=="__main__":
    main()