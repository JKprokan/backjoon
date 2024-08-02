import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
num = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    num[a].append(b)
    num[b].append(a)
count = 0

def bfs(v):
    q = deque([])
    q.append(v)
    visit[v] = 1
    while q:
        x = q.popleft()
        for i in num[x]:
            if visit[i] == 0:
                q.append(i)
                visit[i] = 1

for i in range(1, n+1):
    if visit[i] == 0:
        if not num[i]:
            count += 1
            visit[i] = 1
        else:
            bfs(i)
            count += 1
print(count)