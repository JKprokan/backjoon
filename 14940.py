import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[-1] * m for _ in range(n)]
d = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(h,k):
    q = deque()
    q.append([h,k])
    visit[h][k] = 0
    while q:
        r,c = q.popleft()
        for i in range(4):
            rr = r + d[i][0]
            cc = c + d[i][1]
            if (0<=rr<n) and (0<=cc<m) and visit[rr][cc] == -1:
                if graph[rr][cc] == 0:
                    visit[rr][cc] = 0
                elif graph[rr][cc] == 1:
                    visit[rr][cc] = visit[r][c] + 1
                    q.append([rr,cc])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visit[i][j] == -1:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=" ")
        else:
            print(visit[i][j], end = " ")
    print()

            


