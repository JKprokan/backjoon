import sys
from heapq import heappush, heappop
n = int(input())
hq = []
for i in range(n):
    s = int(sys.stdin.readline())
    if s == 0:
        if hq:
            print(heappop(hq)[1])
        else:
            print(0)
    else:
        heappush(hq, (-s,s))