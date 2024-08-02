from collections import deque
n,k = map(int,input().split())
point = [0]*100001
def bfs():
    q = deque([n])
    while q:
        a = q.popleft()
        if a == k:
            print(point[a])
            break
        for i in (a-1, a+1, a*2):
            if 0<=i<=100000 and not point[i]:
                point[i] = point[a] + 1
                q.append(i)
bfs()  
    