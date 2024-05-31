graph = {
    'S':['B','D','A'],
    'A':['C'],
    'B':['D'],
    'C':['G','D'],
    'D':['G'],
}

def dfs(graph, start, goal):
    visted = []
    stack = [[start]]
    while stack:
        path = stack.pop()
        node = path[-1]
        if node in visted:
            continue
        visted.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node,[])
            for node2 in adjacent_nodes:
                new_path = path.copy()
                new_path.append(node2)
                stack.append(new_path)


sol = dfs(graph,'S','G')
print('Solution is',sol)