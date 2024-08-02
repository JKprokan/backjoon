from collections import deque
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    visited = [0]*10001
    bfs = deque()
    bfs.append([a,""])
    visited[a] = 1
    
    while bfs:
        num, command = bfs.popleft()
        if num == b:
            print(command)
            break
        d = (num*2)%10000
        if not visited[d]:
            visited[d] = 1
            bfs.append([d,command + "D"])
        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = 1
            bfs.append([s,command + "S"])
        l = num//1000 + (num%1000)*10
        if not visited[l]:
            visited[l] = 1
            bfs.append([l,command + "L"])
        r = (num%10)*1000 + num//10
        if not visited[r]:
            visited[r] = 1
            bfs.append([r, command + "R"])