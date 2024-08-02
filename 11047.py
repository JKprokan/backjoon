n,k = map(int,input().split())
arr = []

for i in range(n):
    s = int(input())
    arr.append(s)
count = 0
while k != 0:
    max_coin = max(arr)
    count += k//max_coin
    k = k%max_coin
    arr = [j for j in arr if j <= k]
print(count)
    
