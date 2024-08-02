import sys
sys.setrecursionlimit(1000000)
n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
d = [1,0],[-1,0],[0,1],[0,-1]
a_cnt = 0
b_cnt = 0

def dfs(x,y):
    visited[x][y] = 1
    color = arr[x][y]
    for k in range(4):
        a = x + d[k][0]
        b = y + d[k][1]
        if 0 <= a < n and 0<= b < n and visited[a][b] == 0 and arr[a][b] == color: 
            dfs(a,b)
#일반인
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            a_cnt += 1
#적록색맹
for i in range(n):
    for j in range(n):
        if arr[i][j] == "R":
            arr[i][j] = "G"
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            b_cnt += 1
print(a_cnt, b_cnt)