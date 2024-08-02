from collections import deque
m,n,h = map(int,input().split())
graph = []
q = deque([])
for i in range(h):
    tmp = []
    for j in range(n):
        s = list(map(int,input().split()))
        tmp.append(s)
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i,j,k])
    graph.append(tmp)

dx,dy,dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0] ,[0,0,0,0,1,-1]

while q:
    x,y,z = q.popleft()
    for i in range(6):
        a = dx[i] + x
        b = dy[i] + y
        c = dz[i] + z
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            q.append([a,b,c])
            graph[a][b][c] = graph[x][y][z] + 1
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        day = max(day,max(j))
print(day-1)
