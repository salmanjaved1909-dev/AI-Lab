graph = {
    'S': [('B',5 ), ('A',1)],
    'A': [('C',2)],
    'B': [('G',4)],
    'C': [('G',2)],
    'G': []
}

h = {
    'S': 5,
    'A': 2,
    'B': 4,
    'C': 2,
    'G': 0
}


def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = []

    while queue:
        queue.sort()
        f, g, node, path = queue.pop(0)

        if node in visited:
            continue

        visited.append(node)

        print(node, "g =", g, "h =", h[node], "f =", g + h[node])

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Lowest Cost:", g)
            return

        for child, cost in graph[node]:
            if child not in visited:
                new_g = g + cost
                new_f = new_g + h[child]

                queue.append((new_f, new_g, child, path + [child]))


print("A* Search:")
astar('S', 'G')