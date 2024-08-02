from heapq import heappush, heappop
import sys
t = int(input())
for _ in range(t):
    k = int(input())
    M = []
    m = []
    visited = [0] * 1_000_001
    for i in range(k):
        s = sys.stdin.readline().split()
        if s[0] == "I":
            visited[i] = 1
            heappush(m, (int(s[1]), i))
            heappush(M, (-int(s[1]), i))
        elif s[0] == "D":
            if s[1] =="-1":
                while m and not visited[m[0][1]]:
                    heappop(m)
                if m:
                    visited[m[0][1]] = 0
                    heappop(m)
                    
            else:
                while M and not visited[M[0][1]]:
                    heappop(M)
                if M:
                    visited[M[0][1]] = 0
                    heappop(M)

    while m and not visited[m[0][1]]:
        heappop(m)
    while M and not visited[M[0][1]]:
        heappop(M)

    if len(m)==0 or len(M) == 0:
        print("EMPTY")
    else:
        print(-M[0][0], m[0][0])

