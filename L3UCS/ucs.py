from queue import PriorityQueue

def ucs(start, goal, graph):
    pq = PriorityQueue()
    pq.put((0, start))
    explored = set()
    cost_so_far = {start: 0}
    while not pq.empty():
        current_cost, current_node = pq.get()
        if current_node == goal:
            return current_cost
        if current_node in explored:
            continue
        explored.add(current_node)
        for neighbour, cost in graph[current_node].items():
            new_cost = current_cost + cost
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour]=new_cost
                pq.put((new_cost, neighbour))
    return -1

def get_graph():
    graph={}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = int(input(f"Enter node {i+1}: "))
        graph[node]={}
    m = int(input("Enter the number of edges: "))
    for _ in range(m):
        u, v, w = map(int, input(f"Enter edge {_+1} (u,v,weight): ").split())
        if u in graph:
            graph[u][v]=w
        if v not in graph:
            graph[v]={}
    return graph

if __name__ == "__main__":
    graph = get_graph()
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))
    cost = ucs(start, goal, graph)
    print(f"UCS minimum cost: {cost}")