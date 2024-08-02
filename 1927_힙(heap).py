import heapq
import sys
n = int(input())
heap = []

for i in range(n):
    s = int(sys.stdin.readline())

    if s == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, s)
