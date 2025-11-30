def isvalid(state):
    left, right, boat = state
    if left[0] < left[1] and left[0] > 0:
        return False
    if right[0] < right[1] and right[0] > 0:
        return False
    if left[0] < 0 or left[1] < 0 or right[0] < 0 or right[1] < 0:
        return False
    return True

def successors(state):
    left, right, boat = state
    children = []
    for m in range(3):
        for c in range(3):
            if m+c<1 or m+c>2:
                continue
            if boat == 1:
                nleft = (left[0] - m, left[1] - c)
                nright = (right[0] + m, right[1] + c)
                nboat = 0
            else:
                nleft = (left[0] + m, left[1] + c)
                nright = (right[0] - m, right[1] - c)
                nboat = 1
            child = (nleft, nright, nboat)
            if isvalid(child):
                children.append(child)
    return children

def bfs(state, goal):
    queue = [[state]]
    explored = set()
    explored.add(state)
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        for child in successors(node):
            if child not in explored:
                explored.add(child)
                new_path = path + [child]
                queue.append(new_path)
    return None

if __name__ == "__main__":
    print("Initial state: ")
    lm, lc = map(int, input("Enter the number of missionaries and cannibals on the left bank: ").split())
    rm, rc = map(int, input("Enter the number of missionaries and cannibals on the right bank: ").split())
    l = (lm, lc)
    r = (rm, rc)
    initial = (l, r, 1)
    print("Goal state: ")
    glm, glc = map(int, input("Enter the number of missionaries and cannibals on the left bank: ").split())
    grm, grc = map(int, input("Enter the number of missionaries and cannibals on the right bank: ").split())
    gl = (glm, glc)
    gr = (grm, grc)
    goal = (gl, gr, 0)
    path = bfs(initial, goal)
    for step, node in enumerate(path):
        print(f"Step {step}: {node}")