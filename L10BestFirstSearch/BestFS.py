from queue import PriorityQueue

def bestfs(start, goal, graph, heuristics):
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    explored = set()
    path = []
    while not pq.empty():
        h, node = pq.get()
        if node in explored:
            continue
        explored.add(node)
        path.append(node)
        if node == goal:
            return path
        for neighbour in graph[node]:
            if neighbour not in explored:
                pq.put((heuristics[neighbour], neighbour))
    return path

def get_graph():
    graph = {}
    heuristics = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = int(input(f"Enter node {i+1}: "))
        graph[node]=[]
        heuristics[node]=int(input("Enter heuristics for node: "))
    m = int(input("Enter the number of edges: "))
    for _ in range(m):
        u, v = map(int, input(f"Enter edge {_+1} (u,v): ").split())
        if u in graph:
            graph[u].append(v)
        elif u not in graph:
            graph[u]=[v]
        if v not in graph:
            graph[v]=[]
    return graph, heuristics

if __name__ == "__main__":
    graph, heuristics = get_graph()
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))
    path = bestfs(start, goal, graph, heuristics)
    print(f"Best First Search path: {path}")