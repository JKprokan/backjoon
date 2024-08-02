import sys
n,m = map(int,sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
start,end = 1,max(tree)
while start <= end :
    s = 0
    mid = (start+end) // 2
    for j in tree:
        if j > mid:
            s += (j - mid)
    if s >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)