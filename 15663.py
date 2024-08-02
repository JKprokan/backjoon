from itertools import permutations
n,m = map(int,input().split())
arr = list(map(int,input().split()))

x = list(permutations(arr,m))
x = list(set(x))
x.sort()
for i in x:
    print(" ".join(map(str,i)))