from queue import PriorityQueue

def astar(start, goal, graph, heuristics):
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    came_from = {}
    cost_so_far = {start: 0}
    while not pq.empty():
        current_cost, current_node = pq.get()
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]
        for neighbour, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node]+cost
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                fn = new_cost + heuristics[neighbour]
                pq.put((fn, neighbour))
                came_from[neighbour]= current_node
    return None

def get_graph():
    graph = {}
    heuristics = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = int(input(f"Enter node {i+1}: "))
        graph[node]={}
        heuristics[node]=int(input("Enter heuristics of the node: "))
    m = int(input("Enter the number of edges: "))
    for _ in range(m):
        u, v, w = map(int, input(f"Enter edge {_+1} (u,v): ").split())
        if u in graph:
            graph[u][v]=w
        if v not in graph:
            graph[v]= {}
    return graph, heuristics

if __name__ == "__main__":
    graph, heuristics = get_graph()
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))
    path = astar(start, goal, graph, heuristics)
    print(f"A Star Search path: {path}")