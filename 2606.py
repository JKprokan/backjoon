from collections import deque
com = int(input())
n = int(input())
graph = [[] for _ in range(com+1)]
visited = [0] * (com+1)

for i in range(n):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited[1] = 1
q = deque([1])
while q:
    print(q)
    c = q.popleft()
    
    for j in graph[c]:  
        if visited[j]==0:
            q.append(j)
            visited[j] = 1
print(sum(visited)-1)