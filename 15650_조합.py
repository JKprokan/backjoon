from itertools import combinations
n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
x = list(combinations(arr,m))
for j in x:
    print(" ".join(map(str, j)))

    