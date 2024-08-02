from itertools import combinations_with_replacement
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
x = combinations_with_replacement(arr,m)
for i in x:
    print(" ".join(map(str,i)))