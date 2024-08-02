t = int(input())

def dfs(x, y):
    # 배추 필지 방문 처리
    arr[y][x] = 0

    # 상하좌우 확인
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 1:
            dfs(nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                dfs(j, i)
                count += 1

    print(count)

# t = int(input())

# for _ in range(t):
#     m,n,k = map(int,input().split())
#     arr = [[0 for _ in range(m)] for _ in range(n)]
#     count = 0
#     for _ in range(k):
#         y,x = map(int,input().split())
#         arr[x][y] = 1
#         #print(arr)
#     for j in range(m):
#         for i in range(n):
#             if arr[i][j] == 1:
#                 if i==0:
#                     if j == 0:
#                         if arr[i+1][j] == 1 or arr[i][j+1]== 1:
#                             arr[i][j] = 0
#                     elif j == n-1:
#                         if arr[i][j-1] == 1 or arr[i+1][j] == 1:
#                             arr[i][j] = 0
#                     else:
#                         if arr[i+1][j] == 1 or arr[i][j-1] == 1 or arr[i][j+1]== 1:
#                             arr[i][j] = 0
#                 elif i == n-1:
#                     if j == 0:
#                         if arr[i-1][j] == 1 or arr[i][j+1]== 1:
#                             arr[i][j] = 0
#                     elif j == n-1:
#                         if arr[i][j-1] == 1 or arr[i-1][j] == 1:
#                             arr[i][j] = 0
#                     else:
#                         if arr[i-1][j] == 1 or arr[i][j-1] == 1 or arr[i][j+1]== 1:
#                             arr[i][j] = 0
#                 elif j==0 or j==n-1:
#                     if j ==0:
#                         if arr[i-1][j] == 1 or arr[i][j+1]== 1 or arr[i+1][j]:
#                             arr[i][j] = 0
#                     else:
#                         if arr[i-1][j] == 1 or arr[i][j-1]== 1 or arr[i+1][j]:
#                             arr[i][j] = 0
#                 else:
#                     if arr[i-1][j] == 1 or arr[i+1][j] == 1 or arr[i][j-1] == 1 or arr[i][j+1]== 1:
#                         arr[i][j] = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 1:
#                 count += 1

#     print(count)