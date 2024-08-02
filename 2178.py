import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
s = []
for _ in range(n):
    v = list(input())
    s.append(list(map(int,v)))
visit = [[0] * m for _ in range(n)]
dx =  [[1,0],[-1,0],[0,1],[0,-1]]

def bfs():
    q = deque()
    q.append([0,0])
    visit[0][0] = 1
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            a = dx[i][0] + x
            b = dx[i][1] + y
            if 0<=a<n and 0<=b<m and visit[a][b] == 0:
                if s[a][b] == 1:
                    visit[a][b] = 1 + visit[x][y]
                    q.append([a,b])

bfs()
print(visit[n-1][m-1])
