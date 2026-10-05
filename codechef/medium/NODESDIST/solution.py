N, u, v = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (N + 1)
def dfs(node, distance):
    if node == v:
        return distance
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            result = dfs(neighbor, distance + 1)
            if result != -1:
                return result
    return -1
print(dfs(u, 0))