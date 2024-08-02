from collections import deque
def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        t = q.popleft()
        for k in graph[t]:
            if visited[k] == 0:
                visited[k] = visited[t] + 1
                q.append(k)

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
res = []
for j in range(1, n+1):
    visited = [0]* (n+1)
    bfs(j)
    res.append(sum(visited))
print(res.index(min(res)) +1 )