n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()
for j in range(n):
    print(arr[j])
