def WJSolve(jugs, target, jcap):
    start_state = tuple(jugs)
    explored = set()
    path = dfs(start_state, jcap, target, explored)
    return path

def dfs(cstate, jcap, target, explored):
    j1, j2 = cstate
    if j1 == target or j2 == target:
        return [cstate]
    explored.add(cstate)
    suc = getsuc(cstate, jcap)

    for s in suc:
        if s not in explored:
            path = dfs(s, jcap, target, explored)
            if path is not None:
                return [cstate] + path
    return None

def getsuc(jugs, jcap):
    j1, j2 = jugs
    jc1, jc2 = jcap
    suc = []
    suc.append((jc1, j2))
    suc.append((j1, jc2))
    suc.append((0, j2))
    suc.append((j1, 0))
    pour = min(j1, jc2-j2)
    suc.append((j1-pour, j2+pour))
    pour = min(jc1-j1, j2)
    suc.append((j1+pour, j2-pour))
    return [s for s in suc if isvalid(s, jcap)]

def isvalid(jugs, jcap):
    j1, j2 = jugs
    jc1, jc2 = jcap
    return 0 <= j1 <= jc1 and 0 <= j2 <= jc2

if __name__ == "__main__":
    jc1, jc2 = map(int, input("Enter the jug capacities: ").split())
    j1, j2 = map(int, input("Enter the start state: ").split())
    jcap = (jc1, jc2)
    jugs = (j1, j2)
    target = int(input("Enter the target volume: "))
    path = WJSolve(jugs, target, jcap)
    print(path)