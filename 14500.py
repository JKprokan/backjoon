import sys
n,m = map(int,input().split())
arr = []
visited = [[0]*m for _ in range(n)]
for _ in range(n):
    s = list(map(int, sys.stdin.readline().split()))
    arr.append(s)
d = [(0,1),(0,-1),(1,0),(-1,0)]
dfs_max = 0

def dfs(x,y,sum,c):
    global dfs_max
    if c == 4:
        dfs_max = max(dfs_max,sum)
        return
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny,sum+arr[nx][ny],c+1)
            visited[nx][ny] = 0
    
def exec(i,j):
    global dfs_max
    for l in range(4):
        tmp = arr[i][j]
        for k in range(3):
            t = (l+k)%4
            ni = i + d[t][0]
            nj = j + d[t][1]
            if not (0<=ni<n and 0<=nj<m):
                tmp = 0
                break
            tmp += arr[ni][nj]
        dfs_max = max(dfs_max,tmp)


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,arr[i][j],1)
        visited[i][j] = 0
        exec(i,j)
print(dfs_max)
