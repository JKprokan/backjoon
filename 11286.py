import sys
from heapq import heappush, heappop
n = int(input())
hp = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heappush(hp, (abs(x),x))
    else:
        if hp:
            print(heappop(hp)[1])
        else:
            print(0)