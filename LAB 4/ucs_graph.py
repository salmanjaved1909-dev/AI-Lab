graph = {
    'S': [('B', 4), ('A', 1)],
    'A': [('C', 2)],
    'B': [('G', 1)],
    'C': [('G', 1)],
    'G': []
}


def ucs(start, goal):
    queue = [(0, start, [start])]
    visited = []

    while queue:
        queue.sort()
        cost, node, path = queue.pop(0)

        if node in visited:
            continue

        visited.append(node)

        print(node, "Cost:", cost)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Total Cost:", cost)
            return

        for child, edge_cost in graph[node]:
            if child not in visited:
                new_cost = cost + edge_cost
                queue.append((new_cost, child, path + [child]))

    print("No path found")


print("UCS:")
ucs('S', 'G')