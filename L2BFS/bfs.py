from collections import deque

def bfs(start, visited, graph):
    queue = deque()
    component=[]
    queue.append(start)
    visited[start]=True
    while queue:
        node = queue.popleft()
        component.append(node)
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour]= True
                queue.append(neighbour)
    return component

def get_graph():
    graph={}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = int(input(f"Enter node {i+1}: "))
        graph[node]=[]
    m = int(input("Enter the number of edges: "))
    for _ in range(m):
        u, v = map(int, input(f"Enter edge {_ +1} (u,v): ").split())
        if u in graph:
            graph[u].append(v)
        elif u not in graph:
            graph[u]=[v]
        if v not in graph:
            graph[v]=[]
    return graph

if __name__ == "__main__":
    graph=get_graph()
    visited = {key: False for key in graph}
    start = int(input("Enter the start node: "))
    component= bfs(start, visited, graph)
    print(f"BFS Path: {component}")