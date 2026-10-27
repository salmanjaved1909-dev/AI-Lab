
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


def dfs(node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for child in graph[node]:
            dfs(child, visited)



def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            for child in graph[node]:
                if child not in visited:
                    queue.append(child)


print("DFS:")
dfs('A', [])

print("\nBFS:")
bfs('A')
