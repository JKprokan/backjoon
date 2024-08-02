from collections import deque
n = int(input())
block = []
visit = [[0]*n for _ in range(n)]
for _ in range(n):
    s = list(map(int,list(input())))
    block.append(s)
d = [[1,0],[-1,0],[0,1],[0,-1]]
count = []

def bfs(j,k):
    q = deque()
    q.append([j,k])
    block[j][k] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4): 
            a = d[i][0] + x
            b = d[i][1] + y
            if 0<=a<n and 0<=b<n and block[a][b] == 1:
                block[a][b] = 0
                q.append([a,b])
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if block[i][j] == 1:
            count.append(bfs(i,j))
count.sort()
print(len(count))        
for i in range(len(count)):
    print(count[i])