from collections import deque
n,m = map(int,input().split())
arr = []
visited = []
for _ in range(n):
    arr.append(list(input()))
    visited.append([0]*m)

dir = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(i,j):
    q = deque()
    q.append([i,j])
    cnt = 0
    while q:
        a,b = q.popleft()
        visited[a][b] = 1
        for i in range(4):
            x = dir[i][0] + a
            y = dir[i][1] + b
            if 0<=x<n and 0<=y<m and visited[x][y] == 0 and arr[x][y] != "X":
                visited[x][y] = 1
                q.append([x,y])
                if arr[x][y] == "P":
                    cnt += 1
    if cnt == 0:
        return "TT"
    else:
        return cnt
for j in range(n):
    for k in range(m):
        if arr[j][k] == "I":
            print(bfs(j,k))
            

