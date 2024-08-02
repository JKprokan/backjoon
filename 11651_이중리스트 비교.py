n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([y,x])

s = sorted(arr) 

for y,x in s:
    print(x,y)
