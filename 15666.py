from itertools import combinations_with_replacement
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
x = combinations_with_replacement(arr,m)
x = list(set(x))
x.sort()
for i in x:
    print(" ".join(map(str,i)))
print("adas")