def dfs(node, visited, graph, component):
    component.append(node)
    visited[node]= True
    for child in graph[node]:
        if not visited[child]:
            dfs(child, visited, graph, component)

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
    component=[]
    visited = {key: False for key in graph}
    start = int(input("Enter the start node: "))
    dfs(start, visited, graph, component)
    print(f"DFS Path: {component}")