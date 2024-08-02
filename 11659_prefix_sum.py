import sys 
n,m = map(int,input().split())
s = list(map(int,sys.stdin.readline().split()))
temp = 0
prefix_sum = [0]
for i in s:
    temp += i
    prefix_sum.append(temp)


for _ in range(m):
    i,j = map(int,sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])