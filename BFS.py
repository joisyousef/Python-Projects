graph = {
    'S':['B','D','A'],
    'A':['C'],
    'B':['D'],
    'C':['G','D'],
    'D':['G'],
}

def bfs(graph, start, goal):
    visted = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
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
                queue.append(new_path)

sol = bfs(graph,'S','G')
print('Solution is', sol)