from itertools import permutations
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
x = permutations(arr,m)
for i in x:
    print(" ".join(map(str,i)))