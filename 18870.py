import sys
n = int(input())
x = list(map(int, sys.stdin.readline().split()))
arr = sorted((set(x)))
dic = {}
for i in range(len(arr)):
    dic[arr[i]] = i

for j in x:
    print(dic[j], end = " ")